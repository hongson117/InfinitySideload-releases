# ∞Sideload — Bộ cài USB Windows

[Tải bộ cài](https://github.com/hongson117/InfinitySideload-releases/releases/latest/download/isl-windows.zip) · [Link dự phòng](https://raw.githubusercontent.com/hongson117/InfinitySideload-releases/main/isl-windows.zip) · [Phiên bản và SHA-256](INSTALLERS.json)

Gói hiện tại đóng kèm **∞Sideload 0.1.0 · build 1048**. BUILD-SOURCE.json và INSTALLER-BUILD.json bên trong ZIP ghi phiên bản app và nguồn bộ cài.

## Chuẩn bị

1. Windows 10/11 x64; cài Apple Devices hoặc iTunes chính thức của Apple để có driver USB.
2. Cắm iPhone/iPad bằng cáp dữ liệu, mở khóa và xác nhận **Tin cậy/Trust** khi được hỏi. Remote Pairing cần iOS/iPadOS 17.4+.
3. Giải nén toàn bộ ZIP vào thư mục riêng, giữ các file cạnh nhau trong **isl-windows**. Không chạy launcher trong cửa sổ xem ZIP.

## Chạy bộ cài

Mở **Cai-iSideload.bat**. Launcher kiểm tra checksum trước khi chạy.

| Chế độ | Công việc |
|---|---|
| 1 | Tiếng Việt — ký, cài app và thiết lập ghép đôi |
| 2 | Tiếng Việt — app đã có, chỉ thiết lập/sửa ghép đôi |
| 3 | English — fresh install and pairing |
| 4 | English — repair pairing only |

Với chế độ 1/3, nhập Apple ID, mật khẩu và 2FA trực tiếp trong cửa sổ bộ cài. Mật khẩu được ẩn khi gõ. Người dùng xử lý Chế độ nhà phát triển, khởi động lại và Tin cậy trên iPhone.

Giữ cáp và máy mở khóa đến khi hoàn tất cài app, chuyển file ghép đôi và xác minh. Nếu app đã cài nhưng ghép đôi lỗi, giữ app rồi dùng chế độ 2/4 để tiếp tục.

Trên iPhone, tin cậy nhà phát triển tại **Cài đặt → Cài đặt chung → VPN & Quản lý thiết bị** nếu được hỏi. Mở ∞Sideload, bật Wi-Fi/LocalDevVPN rồi dùng **Cài đặt → Thiết bị & Ghép đôi → Kiểm tra kết nối thiết bị**.

## Kiểm tra ngoại tuyến

- `isl-cli.exe --version`
- `isl-cli.exe --self-test`
- `isl-cli.exe --list-devices`

Self-test không cần tài khoản hay iPhone và không chứng minh cài USB đã hoàn tất. --version là phiên bản CLI; phiên bản app đóng kèm nằm trong metadata của gói. Không gửi mật khẩu, 2FA, .p12 hay pairing record vào chat.

Máy đã có ∞Sideload có thể cập nhật trong **Cài đặt → Cập nhật ∞Sideload**. Xem [hướng dẫn AI](AI-INSTALL.md) nếu có người hỗ trợ.

Nếu Windows chưa nhận iPhone, kiểm tra Apple Devices/iTunes, cáp và Tin cậy. Không tắt antivirus hoặc đổi Execution Policy toàn máy để chạy bộ cài.
