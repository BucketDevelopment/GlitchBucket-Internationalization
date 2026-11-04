<p align="center">
<a href="https://bot.tudubucket.dev"><img src="https://cdn.tudubucket.dev/widebucket.png" width="100%" alt="GlitchBucket"></a>
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
Đây là nơi chứa toàn bộ bản dịch của [GlitchBucket](https://discord.com/application-directory/1103932552701550622). Mỗi ngôn ngữ là một file [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml), được đặt tên theo locale của Discord.

Repo này là **bản sao** của mã nguồn bot và được đồng bộ tự động, nên những gì bạn thấy ở đây luôn giống với bot đang chạy.

## 🍞 Đóng góp bản dịch

Nếu bạn muốn sửa một đoạn dịch, hoặc thêm một ngôn ngữ mới, hãy tạo Pull Request.

Pull Request của bạn sẽ được đưa vào source chính của bot để duyệt. Khi được chấp nhận, Pull Request ở đây cũng sẽ được merge, và bạn vẫn được ghi tên trong commit.

Khi dịch, bạn cần lưu ý:
- **Không sửa `en-US.yaml`**. Đây là bản gốc và được quản lí trong mã nguồn của bot.
- Giữ đúng cấu trúc của `en-US.yaml` (thụt lề, key, ...), và không thêm key mà `en-US.yaml` không có.
- Giữ nguyên các placeholder như `{}`, `{0}`, `{user}`. Bạn có thể đổi vị trí của chúng cho hợp với câu văn, nhưng không được thêm placeholder mới.
- Tên file phải theo [locale của Discord](https://discord.com/developers/docs/reference#locales). Ví dụ, bản dịch tiếng Hindi phải đặt tên là `hi.yaml`.
- Tuân theo giới hạn của Discord:
  + Mô tả lệnh và mô tả tham số tối đa 100 kí tự
  + Placeholder của modal tối đa 100 kí tự
  + Tiêu đề modal tối đa 45 kí tự
  + Không được để trống (ví dụ `my_translation: ''` là không hợp lệ)
  + Xem thêm tại [Discord Developer Docs](https://discord.com/developers/docs/)

Mỗi Pull Request sẽ được kiểm tra tự động theo các quy tắc trên. Nếu bị báo lỗi, bạn chỉ cần sửa theo hướng dẫn trong phần kiểm tra là được.

Lưu ý rằng bản dịch không được làm sai lệch ý nghĩa so với bản gốc `en-US`.
