# Kế Hoạch Tìm Kiếm Email B2B Khách Hàng (Dịch vụ Outsource)

Danh sách `Client_Job.xlsx` chứa dữ liệu của hơn 700+ game studio cùng với link trang Tuyển dụng của họ. Dữ liệu này rất giá trị, tuy nhiên nó chưa chứa trực tiếp email của những người ra quyết định. 

Để gửi email marketing mời chào dịch vụ Outsource (như Art, Animation, Programming) thành công, bạn cần lấy được email của **Art Director, Technical Director, Producer, hoặc Studio Head**. Gửi vào email hỗ trợ (info@, jobs@) thường có tỷ lệ phản hồi thấp.

Dưới đây là kế hoạch chi tiết tự động hóa và tối ưu hóa việc tìm kiếm email:

## Yêu cầu xem xét (User Review Required)

> [!IMPORTANT]
> **Quyết định sử dụng dịch vụ trả phí hay miễn phí?**
> Các phương pháp miễn phí (Web Scraping) sẽ chỉ lấy được các email dùng chung (contact@, info@). Để lấy được email của cá nhân cấp cao (vd: john.doe@10chambers.com), việc dùng API trả phí của các nền tảng thông tin B2B (như Apollo.io, Hunter.io) là BẮT BUỘC. Bạn có sẵn sàng sử dụng các tài khoản API này không?

> [!WARNING]
> **Rủi ro về Spam**
> Gửi email hàng loạt không chọn lọc sẽ làm hỏng uy tín domain của bạn (Domain Reputation), khiến mọi email sau này bị rơi vào mục Spam. Kế hoạch này sẽ bao gồm cả bước xác thực (Verify) email trước khi gửi.

---

## Chi tiết Kế hoạch (Proposed Changes)

Quá trình chia làm 4 giai đoạn, tôi có thể bắt tay vào lập trình tự động hóa các bước này cho bạn bằng Python ngay sau khi bạn đồng ý:

### Giai đoạn 1: Tiền xử lý dữ liệu (Data Preprocessing)
- **Tổng hợp Sheet:** Trích xuất toàn bộ dữ liệu từ tất cả các tab ("Studios Hiring now", "Latest Jobs posts"...) trong file excel.
- **Trích xuất Domain:** Dùng biểu thức chính quy (Regex) và bot để trích xuất tên miền gốc từ cột Link. *(VD: `https://careers.10chambers.com/jobs` ➔ `10chambers.com`)*.
- **Làm sạch:** Loại bỏ các studio trùng lặp, xuất ra 1 file CSV chuẩn hoá `Cleaned_Target_Studios.csv` gồm: Tên Studio, Domain, Quốc gia để làm đầu vào cho các tool tìm kiếm.

#### [NEW] `e:\TDC_App\TDGAMES_App\Client_Data\data_cleaning_script.py`
Code Python dùng `pandas` và `urllib` để dọn dẹp và chuẩn bị file data hạt giống.

---

### Giai đoạn 2: Khai phá & Dò tìm Email (Email Discovery)

Tùy vào ngân sách và lựa chọn của bạn, chúng ta có 2 phương án (có thể kết hợp):

- **Cách 1 - Quét Web (Web Scraping - Miễn phí):** 
  - Viết 1 script Python dùng để tự động duyệt qua website gốc của từng studio.
  - Tìm kiếm thông tin liên hệ tĩnh (các thẻ `mailto:` hoặc bắt regex dạng `@domain.com`) ở các trang `/contact`, `/about-us`, `/partners`.
  - Phù hợp để lấy các email B2B chung như `partners@`, `outsource@`, `bizdev@`.

- **Cách 2 - Sử dụng B2B Database API (Tỷ lệ chuyển đổi cao nhất):**
  - Sử dụng API của nền tảng như **Apollo.io** (chuyên tìm ngách chức danh) hoặc **Hunter.io**.
  - Script sẽ truyền Domain vào API, tuỳ chọn lọc theo "Job Title" bao gồm các từ khóa: `"Outsource", "Producer", "Art Director", "Technical Director"`.
  - Kết quả trả lại email đích danh của người chịu trách nhiệm thuê ngoài. 

#### [NEW] `e:\TDC_App\TDGAMES_App\Client_Data\email_discovery_bot.py`
Công cụ gọi API hàng loạt hoặc Scraping để điền thêm cột "Contact Email" vào danh sách.

---

### Giai đoạn 3: Xác thực Email (Email Verification & Validation)
- Để bảo vệ tên miền gửi mail, những email tìm được sẽ chạy qua một công cụ Check Spam nội bộ để thử PING tới Mail Server xem email đó còn tồn tại thực sự hay không.
- Loại bỏ các mail "catch-all" rác.

#### [NEW] `e:\TDC_App\TDGAMES_App\Client_Data\email_verifier.py`
Code kiểm tra (SMTP Verification) các cấu hình DNS mail (MX record) trước khi lưu vào danh sách cuối.

---

### Giai đoạn 4: Xuất Danh Sách Cho Chiến Dịch Marketing
- Tổng hợp thành file `Verified_Outsource_Leads.xlsx` nhập sẵn định dạng tương thích với các nền tảng dội bom Email Marketing như Mailchimp, Lemlist, SendGrid. Có sẵn các field Name, Role, Studio.. để Cá nhân hoá (Personalized) nội dung mail tự động.

## Câu hỏi mở (Open Questions)

> [!NOTE]
> 1. Bạn ưu tiên phương án tìm kiếm Web Scraping (miễn phí nhưng chỉ ra email chung) hay API bên thứ ba (Apollo.io/Hunter.io - tỷ lệ trúng người quản lý cao)? Nếu dùng API, bạn đã có API Key chưa?
> 2. Có đối tượng cụ thể nào (Chuyên môn 2D/3D Art, hay Programming, QA) mà dịch vụ Outsource của bạn đang tập trung vào không? Thông tin này sẽ giúp filter chính xác các chức danh cần lấy email thay vì lấy HR chung chung.

## Verification Plan

### Kế hoạch Kiểm chứng:
- Sau khi viết Code **Giai đoạn 1**, tôi sẽ in ra output thử nghiệm của 15 Studio ngẫu nhiên để verify xem việc lấy Domain có đúng chuẩn không.
- Code **Giai đoạn 2**, thử nghiệm trên quy mô 10-20 domain trước, trả về file kết quả nháp đảm bảo logic lấy email / check email hoạt động mượt mà.
- Review kết quả nháp này cùng bạn và quyết định xem chất lượng email thu được đã đủ để chạy hàng loạt (hơn 700 công ty) chưa.
