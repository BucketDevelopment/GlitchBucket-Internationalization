"""Validate localization files against en-US.yaml.

Usage: python scripts/validate.py [--baseline DIR] [file.yaml ...]   (default: every locale file)

Errors fail the check; warnings are only printed. With --baseline, errors that already exist
in the same file under DIR (e.g. the target branch) are reported as warnings instead.
"""
import re
import sys
import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BASE = 'en-US.yaml'
PLACEHOLDER = re.compile(r'\{[^{}\s]*\}')
LOCALE_FILE = re.compile(r'^[a-z]{2}(-[A-Z]{2})?\.yaml$')

# (rule name, matcher on the key path, max length)
LIMITS = [
    ('command description', lambda p: 'commands' in p and p[-1] == 'description', 100),
    ('option description', lambda p: 'describe' in p, 100),
    ('choice name', lambda p: 'choices' in p, 100),
    ('modal title', lambda p: 'modals' in p and p[-1] == 'title', 45),
    ('modal label', lambda p: 'modals' in p and p[-1] in ('label', 'text'), 45),
    ('placeholder', lambda p: p[-1] == 'placeholder', 100),
]


def flatten(node, path=()):
    if isinstance(node, dict):
        for key, value in node.items():
            yield from flatten(value, path + (str(key),))
    else:
        yield path, node


def placeholders(text: str) -> set[str]:
    # str.format treats "{}" as the next positional index, so "{}" and "{0}" are interchangeable
    result, index = set(), 0
    for match in PLACEHOLDER.findall(text):
        if match == '{}':
            result.add(f'{{{index}}}')
            index += 1
        else:
            result.add(match)
    return result


def load(path: Path):
    with path.open(encoding='utf-8') as file:
        return yaml.safe_load(file) or {}


def check(path: Path, base: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    if not LOCALE_FILE.match(path.name):
        errors.append(f'{path.name}: file name must be a Discord locale id, e.g. vi.yaml, pt-BR.yaml')

    try:
        data = load(path)
    except yaml.YAMLError as e:
        return [f'{path.name}: invalid YAML: {e}'], []

    for key_path, value in flatten(data):
        key = '.'.join(key_path)
        if key_path not in base:
            errors.append(f'{path.name}: {key}: key does not exist in {BASE}')
            continue

        original = base[key_path]
        if original is None or original == '':
            continue  # empty in the base file, nothing to compare against

        if isinstance(original, list):
            if not isinstance(value, list) or not value or not all(isinstance(v, str) and v.strip() for v in value):
                errors.append(f'{path.name}: {key}: must be a non-empty list of strings like {BASE}')
            continue

        if not isinstance(value, str) or not value.strip():
            errors.append(f'{path.name}: {key}: value must be a non-empty string')
            continue

        if isinstance(original, str):
            expected, got = placeholders(original), placeholders(value)
            if got - expected:
                errors.append(f'{path.name}: {key}: unknown placeholders {sorted(got - expected)}, {BASE} only has {sorted(expected)}')
            if expected - got:
                warnings.append(f'{path.name}: {key}: placeholders {sorted(expected - got)} from {BASE} are not used')

            for name, matches, limit in LIMITS:
                # only enforce when the base text itself respects the limit, so plain message keys are not caught
                if matches(key_path) and len(original) <= limit < len(value):
                    errors.append(f'{path.name}: {key}: {name} is {len(value)} characters, Discord allows {limit}')

    missing = [k for k in base if k not in dict(flatten(data))]
    if missing:
        warnings.append(f'{path.name}: {len(missing)} keys are not translated yet (falls back to {BASE})')

    return errors, warnings


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('files', nargs='*')
    args = parser.parse_args(argv)

    base = dict(flatten(load(ROOT / BASE)))
    files = [ROOT / name for name in args.files] if args.files else sorted(p for p in ROOT.glob('*.yaml') if p.name != BASE)

    errors, warnings = [], []
    for path in files:
        if path.name == BASE:
            continue
        e, w = check(path, base)
        if args.baseline and (args.baseline / path.name).exists():
            known = set(check(args.baseline / path.name, base)[0])
            w += [f'{line} (already on the target branch)' for line in e if line in known]
            e = [line for line in e if line not in known]
        errors += e
        warnings += w

    for line in warnings:
        print(f'warning: {line}')
    for line in errors:
        print(f'error: {line}')
    print(f'{len(files)} file(s) checked, {len(errors)} error(s), {len(warnings)} warning(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
