# Hỗ trợ cài ∞Sideload trên Windows và macOS

Kho phân phối chính thức: [hongson117/InfinitySideload-releases](https://github.com/hongson117/InfinitySideload-releases).

Phiên bản app và checksum bộ cài đang phát hành được ghi trong [INSTALLERS.json](INSTALLERS.json). Trong mỗi ZIP, `BUILD-SOURCE.json` xác định app đóng kèm và `INSTALLER-BUILD.json` ghi nguồn bộ cài, phiên bản app và SHA-256 của IPA. Phiên bản CLI hiển thị bởi `--version` có thể khác phiên bản app iPhone.

## Tải và xác minh

- [Windows ZIP](https://github.com/hongson117/InfinitySideload-releases/releases/latest/download/isl-windows.zip) · [Mirror](https://raw.githubusercontent.com/hongson117/InfinitySideload-releases/main/isl-windows.zip).
- [macOS Universal ZIP](https://github.com/hongson117/InfinitySideload-releases/releases/latest/download/isl-macos-universal.zip) · [Mirror](https://raw.githubusercontent.com/hongson117/InfinitySideload-releases/main/isl-macos-universal.zip).
- [Checksum hai ZIP](SHA256SUMS.txt). Checksum bên trong ZIP áp dụng cho các file của gói đó.

Đọc manifest, chọn đúng hệ điều hành và đối chiếu SHA-256 trước khi chạy. Giải nén toàn bộ vào thư mục mới, giữ các file cạnh nhau. Không sửa checksum để bỏ qua lỗi.

## Chọn chế độ

| Nhu cầu | Tiếng Việt | English |
|---|---:|---:|
| Cài từ đầu, ký app và thiết lập Remote Pairing | 1 | 3 |
| App đã có, chỉ thiết lập/sửa ghép đôi | 2 | 4 |

Windows mở **Cai-iSideload.bat**; macOS mở **Cai-iSideload.command**. Gói đã có Sideload.ipa kèm các thành phần chạy app cùng phiên bản.

## Quy trình hỗ trợ

1. Xác nhận công cụ đang chạy trên máy Windows/Mac thực sự cắm iPhone. Terminal cloud không tự nhìn thấy USB của người dùng.
2. Windows cần Windows 10/11 x64 và Apple Devices hoặc iTunes có driver USB. Mac Universal hỗ trợ Apple Silicon/Intel, macOS 11+. Remote Pairing cần iOS/iPadOS 17.4+.
3. Người dùng cắm cáp dữ liệu, mở khóa và xác nhận Tin cậy trên iPhone/Finder khi được hỏi.
4. Mở launcher trong Terminal/console tương tác để người dùng nhập trực tiếp. Không chạy luồng đăng nhập ở nền.
5. Apple ID, mật khẩu, 2FA và mật mã iPhone do người dùng nhập trong bộ cài/iPhone. Không yêu cầu dán vào chat, ghi log hoặc commit. Không chia sẻ .p12, pairing record hay cache tài khoản.
6. Người dùng xử lý Chế độ nhà phát triển, khởi động lại và xác nhận nhà phát triển. Không tự thu hồi chứng chỉ hoặc gỡ app để chữa lỗi.
7. Giữ cáp đến khi hoàn tất chuyển và xác minh file ghép đôi. Dòng “App đã cài” chưa chứng minh bước ghép đôi đã xong.
8. Mở ∞Sideload, đăng nhập tài khoản của chủ máy nếu cần tự gia hạn. Giữ Wi-Fi bật, bật LocalDevVPN rồi chọn **Cài đặt → Thiết bị & Ghép đôi → Kiểm tra kết nối thiết bị**.
9. Báo riêng kết quả self-test, cài app, ghép đôi USB và kiểm tra LocalDevVPN. Không coi self-test ngoại tuyến là xác nhận cài trên thiết bị thật.

## Lệnh kiểm tra

Windows: `isl-cli.exe --version`, `isl-cli.exe --self-test`, `isl-cli.exe --list-devices`.

macOS: `./isl-mac --version`, `./isl-mac --self-test`, `./isl-mac --list-devices`.

Self-test không cần tài khoản hay iPhone. **--pair-only** có ghi trạng thái ghép đôi và không phải kiểm tra chỉ đọc. Nếu app đã cài nhưng ghép đôi chưa xong, giữ app và dùng chế độ 2/4 sau khi xử lý nguyên nhân. Không đặt lại trust chỉ vì lần mở app này chưa kiểm tra kết nối.

## Cập nhật app

Vào **Cài đặt → Cập nhật ∞Sideload → Kiểm tra phiên bản mới ngay → Tải, ký và cập nhật**. App kiểm tra SHA-256 rồi ký bằng nguồn gia hạn của bản đang cài. Đổi chủ sở hữu/Apple ID là luồng riêng.

Từ gói 1048, bộ tải có đường GitHub API dự phòng. Nếu cả đường chính và API đều lỗi, app báo lỗi thay vì tiếp tục với file tải thiếu.

Xem thêm [Windows](WINDOWS.md), [macOS](MACOS.md), [giới hạn cài đặt](INSTALL-LIMITS.md) và [khôi phục chứng chỉ](CERTIFICATE-RECOVERY.md).
