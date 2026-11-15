# Giới hạn cài đặt: thiết bị quyết định

Bỏ chặn trước khi cài dựa vào số app trong danh sách cục bộ. Danh sách này chỉ là lịch sử do app quản lý; không xác định chắc profile miễn phí/trả phí, quota trên máy hay hành vi từng phiên bản hệ điều hành. Số app theo từng tài khoản chỉ để hiển thị, không phải số slot còn trống.

Khi chọn Apple ID B, dùng đúng thông tin đăng nhập/Team/chứng chỉ của B và gửi yêu cầu cài thực tế. Không tự chuyển sang A hoặc tự thu hồi chứng chỉ để lách quota. Khi hệ điều hành/Apple từ chối, giữ lỗi gốc và đưa hướng dẫn theo loại lỗi. Không tự suy ra tổng 3 app cho mọi tài khoản hoặc mọi nền tảng từ một thông báo quota chung.

Giới hạn App ID của tài khoản và giới hạn ứng dụng đang cài là hai loại lỗi riêng. Trường hợp lỗi chứa cả Remote Pairing và installed-app quota phải được báo là quota, không hướng dẫn tạo lại pairing. Kiểm thử Rust bao phủ phân loại này.

Sửa chốt chặn của ứng dụng không thay đổi chính sách Apple hoặc hệ điều hành. Chưa kiểm chứng lượt cài app thứ tư trên iPhone bằng nhiều Apple ID. Kết quả người dùng trên Apple TV là dữ liệu riêng cho tvOS; không suy ngược thành cam kết áp dụng cho iOS. Bản iSideload này vẫn là iPhone/iPad và từ chối IPA tvOS-only.

## Phân biệt 3 giới hạn riêng của Apple ID miễn phí (vì sao vẫn báo hết chứng chỉ khi còn nhiều App ID)

1. **Chứng chỉ phát triển (`Development Certificate`):** Tối đa **1 chứng chỉ** hoạt động cùng lúc cho toàn bộ Apple ID (mã lỗi Apple `7460` / *Maximum Development Certificates Reached*).
2. **App ID:** Tối đa **10 App ID** mỗi **7 ngày** (tự nhả sau 7 ngày).
3. **Số ứng dụng đang cài trên mỗi máy:** Tối đa **3 ứng dụng** sideload hoạt động đồng thời (`∞Sideload` dùng tối đa 3 suất này cho **Chính + Phụ 1 + Phụ 2**).

Do giới hạn **1 chứng chỉ**, khi mới cài từ Windows/macOS sang iPhone/iPad, bộ cài PC/Mac đã lấy suất chứng chỉ duy nhất (`iSideload Windows` / `iSideload macOS`). Lần đầu mở app trên iPhone/iPad và tự ký (cài Phụ 1 hoặc gia hạn), app cần **thu hồi** chứng chỉ tạm của PC/Mac để tạo chứng chỉ riêng trên iPhone/iPad (ưu tiên chạy qua **Cài đặt → Gia hạn ∞Sideload**, hoặc chạy ngay bước đó trước khi vuốt đóng app để bản Chính cũng được ký lại sang chứng chỉ mới). Mỗi máy nên dùng **1 Apple ID miễn phí riêng**.
