<p align="center">
<a href="https://bot.tudubucket.dev"><img src="https://cdn.langdua.net/104169263_p1.png" height="auto" width="180" style="border-radius:50%"></a>
</p>

<h1 align="center">GlitchBucket Internationalization</h1>
<p align="center">Bản dịch ngôn ngữ cho GlitchBucket.</p>

<div align="center">
    <a href="https://discord.gg/Yq6TT6bjX7"><img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=f5f5f5" alt="Discord"/></a>
    <a href="https://tudubucket.dev/application"><img src="https://img.shields.io/badge/Add_GlitchBucket-C0CDFF?style=for-the-badge&logo=robotframework&logoColor=gray" alt="Add Bot"/></a>
    <br>
    <img src="https://img.shields.io/github/last-commit/BucketDevelopment/GlitchBucket-Internationalization?style=for-the-badge" alt="GitHub last commit"/>
    <img src="https://img.shields.io/github/commit-activity/w/BucketDevelopment/GlitchBucket-Internationalization?style=for-the-badge" alt="GitHub commit activity"/>
    <img src="https://img.shields.io/github/commit-activity/t/BucketDevelopment/GlitchBucket-Internationalization?style=for-the-badge" alt="GitHub commit activity"/>
    <br>
</div>

## 🌺 Giới thiệu
Repo này chứa bản dịch của [GlitchBucket](https://discord.com/application-directory/1103932552701550622). Mỗi ngôn ngữ là một file [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml), đặt tên theo locale ID của Discord.

Repo này là bản sao (mirror) được đồng bộ tự động từ mã nguồn của bot, nên nhánh `main` luôn khớp với bản bot đang chạy.

## 🍞 Đóng góp bản dịch

Tạo Pull Request để sửa hoặc thêm bản dịch. PR sau khi được duyệt sẽ được đưa vào mã nguồn của bot, sau đó repo này tự cập nhật và PR được đóng kèm liên kết. Bạn vẫn được ghi công trong commit.

Khi sửa hoặc thêm file, hãy đảm bảo:
- Không sửa `en-US.yaml`. Đây là bản gốc, do mã nguồn của bot quản lý.
- Giữ đúng cấu trúc của `en-US.yaml` (thụt lề, key, ...). Không thêm key không có trong `en-US.yaml`.
- Giữ nguyên số lượng và thứ tự `{}` cũng như các placeholder dạng `{user}`, `{channel}`.
- Tên file theo [Discord Locales](https://discord.com/developers/docs/reference#locales). Ví dụ bản dịch tiếng Hindi phải đặt tên `hi.yaml`.
- Tuân theo giới hạn của Discord:
  + Mô tả lệnh dưới 100 ký tự
  + Mô tả tham số lệnh dưới 100 ký tự
  + Placeholder của modal dưới 100 ký tự
  + Tiêu đề modal dưới 45 ký tự
  + Không để trống key (ví dụ `my_translation: ''` là không hợp lệ)
  + Xem thêm tại [Discord Developer Docs](https://discord.com/developers/docs/)

Bản dịch không được làm sai lệch ý nghĩa so với bản gốc `en-US`.
