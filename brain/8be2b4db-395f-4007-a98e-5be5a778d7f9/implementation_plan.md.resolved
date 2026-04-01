# Kế hoạch triển khai: Ứng dụng Lưu trữ & Preview Animation (Spine)

Ứng dụng: `Spine_Preview_App` (phục vụ khách hàng xem trước toàn bộ các nhân vật Animation).

## Trả lời các lựa chọn của bạn:

### 1. Về vị trí thư mục và Lỗi quyền truy cập
Bạn đồng ý tạo tại `e:\TDC_App\TDGAMES_App\Spine_Preview_App`. Tuy nhiên, hiện tại **tôi chỉ được cấp quyền thao tác bên trong thư mục `Review_Feedback_App`**.
Để tôi có thể tạo thư mục `Spine_Preview_App` nằm cùng cấp, bạn có 2 lựa chọn:
- **Phương án A:** Bạn vào cài đặt của công cụ AI này, **tắt tính năng "Workspace Validation"** (Kiểm tra không gian làm việc).
- **Phương án B:** Bạn tự mở Terminal ở `e:\TDC_App\TDGAMES_App\` và gõ lệnh: `npm create vite@latest Spine_Preview_App -- --template react-ts`. Sau đó mở thư mục đó vào IDE và tôi sẽ bắt đầu code.

### 2. Supabase có tác dụng gì? Có bắt buộc không?
Bởi vì **Google Drive không hỗ trợ load file Spine lên web** (do lỗi CORS chặn bảo mật), bạn **bắt buộc phải có một nơi lưu trữ file chuẩn**. Bạn có 2 hướng đi:

- **Hướng 1 - Không dùng Supabase (Hardcode - Tĩnh):** Bạn copy thủ công các file Spine (`.json`, `.atlas`, `.png`) vào thư mục `public/` của dự án.
  - *Ưu điểm:* Cực kỳ đơn giản, không cần server, không cần database. Code xong là chạy.
  - *Nhược điểm:* Mỗi khi có nhân vật mới, bạn phải copy file vào thư mục code, sửa code danh sách và **phải build lại/deploy lại Web**.

- **Hướng 2 - Dùng Supabase (Dynamic - Hiện đại):** Dùng Supabase làm ổ đĩa lưu trữ (Storage) và cơ sở dữ liệu (Database) danh sách nhân vật.
  - *Ưu điểm:* Bạn có một trang Quản trị (Admin) để ấn nút "Upload nhân vật mới". Web của khách sẽ tự động cập nhật ngay lập tức mà **không cần đụng vào code**.
  - *Nhược điểm:* Tốn công setup ban đầu hơn một chút.

> [!TIP]
> **Đề xuất của tôi:** Ban đầu, nếu chưa có nhiều dự án, chúng ta hãy chọn **Hướng 1 (Tĩnh)** để có sản phẩm nhanh, mượt. Sau này lúc nào cần mở rộng thì tích hợp Supabase sau (mất 30 phút).

### 3. Về UI/Styling (TailwindCSS)
Vì bạn muốn phương án tối ưu nhất, tôi sẽ chọn **TailwindCSS**. Đây là tiêu chuẩn hiện tại, giúp code trang Web cực sạch, Load rất nhanh và dễ tạo các hiệu ứng hiện đại siêu đẹp (như Glow, Glassmorphism).

---

## 🏗️ Kiến trúc ứng dụng (Hướng 1 - Tĩnh)

- **Công nghệ:** React 19 + TypeScript + Vite + TailwindCSS.
- **Animation Engine:** `@esotericsoftware/spine-webgl`.
- **Cấu trúc:**
  - `public/characters/`: Thư mục lưu file spine (VD: `hero.json`, `hero.atlas`).
  - `src/data/characters.ts`: File định nghĩa danh sách nhân vật hiển thị trên Web.
  - `src/pages/GalleryPage.tsx`: Trang lưới grid siêu đẹp trưng bày các Card nhân vật.
  - `src/pages/ViewerPage.tsx`: Trang chi tiết có cửa sổ 3D để test Spine.

## User Review Required

> [!CAUTION]
> **Vui lòng trả lời 2 vấn đề sau để tôi code ngay:**

1. Tôi đã bị chặn quyền tạo thư mục bên ngoài. Bạn sẽ **tắt tính năng "Workspace Validation"** trong Cài đặt (Settings), hay muốn bạn **tự gõ lệnh tạo dự án**?
2. Chốt lại chúng ta làm theo **Hướng 1 (Không dùng Supabase - để file trong máy tính/thư mục public)** cho nhanh gọn nhất giai đoạn này nhé?
