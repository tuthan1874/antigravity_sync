# Bàn giao: Ứng dụng Spine Preview App (Phase 1)

Dự án mới đã được xây dựng và đang chạy thành công tại địa chỉ **http://localhost:5173/**. Toàn bộ logic lưu trữ cũ đã được backup, ứng dụng mới được thiết kế hoàn toàn theo tiêu chuẩn Glassmorphism tối giản và siêu mượt với **TailwindCSS v4**.

## Các thành phần đã hoàn thiện

### 1. Giao diện người dùng (UI Component)
- **App Layout:** Sidebar và Main Panel được thiết kế theo phong cách kính mờ (Glassmorphism), viền sáng, đổ bóng, gradient glow ở background, sử dụng Lucide React Icon.
- **Gallery Page (Trang chủ):**
  - Hiển thị danh sách các thẻ bài (Cards) chứa thông tin mô hình (Title, Description).
  - Background của Card là chính hình Thumbnail của mô hình đó.
  - Hiệu ứng Animation khi rê chuột siêu mượt mà.
- **Spine Viewer Page (Trang Xem Chi Tiết):**
  - Tích hợp thành công **Spine WebGL** engine.
  - Sidebar mini điều khiển Animation State và Skin.
  - Hỗ trợ Play/Pause, Reset Camera, Phóng to/Thu nhỏ (Zoom/Pan).

### 2. Kiến trúc Data & Backend (Supabase + Cloudflare R2)

Ngay lúc này, dữ liệu Data Source đang được trỏ tới File chứa Data ảo (Mock Data) vì chưa có Keys của Supabase. Tuy nhiên, kiến trúc Data đã được setup 100%.

#### Cấu trúc Bảng `characters` trên Supabase
Bạn vui lòng tạo 1 bảng tên `characters` với các cột sau:
- `id` (uuid, khóa chính)
- `created_at` (timestamp, tự sinh)
- `name` (text) - Tên nhân vật (VD: Raptor)
- `description` (text) - Mô tả (VD: Mô hình khủng long)
- `thumbnail_url` (text) - Link ảnh đại diện (Lấy từ Cloudflare R2)
- `skeleton_url` (text) - Link file `.json` hoặc `.skel` (Lấy từ Cloudflare R2)
- `atlas_url` (text) - Link file `.atlas` (Lấy từ Cloudflare R2)
- `texture_url` (text) - Link file `.png` (Lấy từ Cloudflare R2)
- `status` (text) - Điền là `published` hoặc `draft`

## User Checklist
> [!IMPORTANT]
> **Các bước tiếp theo bạn cần làm để kết nối Real Data:**
> 1. Truy cập vào trang quản trị Supabase của bạn, chạy SQL tạo bảng như hướng dẫn ở trên.
> 2. Lấy `URL` và `ANON_KEY` của project Supabase.
> 3. Tạo một file tên là `.env.local` ở ngoài cùng thư mục dự án này, dán 2 dòng sau vào:
>    `VITE_SUPABASE_URL=link_cua_ban`
>    `VITE_SUPABASE_ANON_KEY=key_cua_ban`
> 4. Restart lại dự án. App của bạn sẽ chính thức chạy Real Data thay vì Demo Data!

Trải nghiệm App ngay tại trình duyệt của bạn (Tab "Localhost"). Nếu cần chỉnh sửa thêm tính năng upload trực tiếp (Admin Dashboard), hãy báo cho tôi nhé!
