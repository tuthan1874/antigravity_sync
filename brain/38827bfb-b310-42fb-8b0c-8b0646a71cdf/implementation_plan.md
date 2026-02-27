# Thêm màn hình Đăng nhập bằng NocoDB Account

Mục tiêu: Bảo vệ ứng dụng bằng màn hình đăng nhập, sử dụng bảng `Account` trên NocoDB để lưu trữ tài khoản (username/password).

## User Review Required
> [!NOTE]
> Ứng dụng sẽ yêu cầu đăng nhập trước khi hiển thị giao diện chính. Các API phía backend (như load cấu hình, trigger sync thủ công từ web) cũng sẽ được bảo vệ bằng Token (JWT). Các webhook từ Slack/ClickUp vẫn hoạt động bình thường mà không cần đăng nhập ngầm. Bạn xem qua chi tiết các file sẽ thay đổi dưới đây nhé.

## Proposed Changes

### NocoDB
- Tạo bảng **Account** trên NocoDB (Base ID: `pjlxcpr5ih0q9y9`) với các cột cơ bản:
  - `username` (SingleLineText)
  - `password` (SingleLineText) - hiện tại chưa mã hoá theo yêu cầu
  - `name` (SingleLineText) - tên hiển thị (VD: "Admin")
- Thêm 1 bản ghi mặc định (VD: admin/admin) để test.

---

### Backend (Node.js)
Sử dụng thư viện phổ biến `jsonwebtoken` (JWT) để quản lý phiên đăng nhập an toàn, thay vì cài cắm session phức tạp cho ứng dụng đơn giản.

#### [MODIFY] package.json
Thêm thư viện `jsonwebtoken` để mã hoá/giải mã token đăng nhập.

#### [NEW] src/middleware/auth.js
Tạo middleware kiểm tra token. Bất kỳ request nào vào `/api/*` (trừ Login) đều phải có header `Authorization: Bearer <token>`. Nếu không có hoặc token sai, trả về lỗi 401.

#### [MODIFY] src/api.js
- Thêm route POST `/login`: 
  - Gọi tới NocoDB, truy vấn bảng `Account` tìm `username` và `password`.
  - Nếu đúng, tạo JWT token trả về cho Frontend.
- Tích hợp `authMiddleware` chặn các route còn lại (cấu hình, khách hàng, project, log...).

---

### Frontend (Giao diện & Logic)
Chỉnh sửa giao diện Single Page Application (SPA) hiện tại.

#### [MODIFY] public/index.css
- Thêm CSS cho màn hình đăng nhập (chứa logo ChatSync, form username/password đẹp mắt).
- Màn hình này sẽ che toàn bộ màn hình chính (`z-index: 9999`) cho đến khi đăng nhập thành công.

#### [MODIFY] public/index.html
- Thêm DOM overlay cho màn hình `login-overlay` trước cấu trúc `sidebar` và `main-content`. Nhập username, password và nút Đăng nhập.

#### [MODIFY] public/app.js
- **Check Auth khi load trang:** Kiểm tra `localStorage.getItem('token')`.
  - Nếu có: Ẩn login overlay, load dashboard.
  - Nếu không: Hiện login overlay.
- **Form Submit:** Gửi request POST tới `/api/login`. Thành công -> bật dashboard. Thất bại -> báo lỗi.
- **Sửa hàm fetchAPI():** Tự động đính kèm `Authorization: Bearer <token>` vào mọi request gửi lên server. Bắt lỗi HTTP 401 (hết hạn token) để logout người dùng.
- Thêm nút **Đăng xuất (Logout)** ở sidebar.

## Verification Plan

### Manual Verification
1. Mở trang web dạng Ẩn danh (Incognito), giao diện Dashboard sẽ KHÔNG hiện ra, mà bị chặn lại bởi form Login.
2. Thử nhập sai user/pass -> Form báo lỗi.
3. Đăng nhập đúng `admin/admin` -> Giao diện chính mở ra, dữ liệu bảng load bình thường.
4. Refresh trang lại -> Vẫn giữ đăng nhập.
5. Sửa dữ liệu (VD: thêm Khách hàng mới) -> Ghi nhận thành công.
6. Test các webhook (ClickUp -> Slack) xem còn hoạt động bình thường không (Đảm bảo việc thêm Auth không chặn webhook).
