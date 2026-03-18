# TD Games Billing App — Phân Tích Tính Năng Còn Thiếu & Cần Cải Thiện

---

## 📄 1. Invoice App (Hoàn thiện nhất — ít thiếu)

| Ưu tiên | Tính năng | Mô tả |
|---------|----------|-------|
| 🟡 | **Dashboard nâng cao** | Thêm biểu đồ doanh thu theo tháng/quý, tỷ lệ paid vs pending, doanh thu theo client/studio |
| 🟡 | **Search & Sort trong History** | Cho phép tìm kiếm theo invoice number, sort theo ngày / giá trị |
| 🟢 | **Multi-currency dashboard** | Hiển thị tổng doanh thu tách biệt USD & VND, tổng quy đổi |
| 🟢 | **Reminder/notification** | Nhắc nhở hoá đơn sắp đến hạn hoặc quá hạn (overdue alerts) |
| 🟢 | **Bulk actions** | Chọn nhiều hoá đơn để xoá / mark as paid cùng lúc |

---

## 💰 2. Expense App (Cần cải thiện nhiều)

| Ưu tiên | Tính năng | Mô tả |
|---------|----------|-------|
| 🔴 | **Dashboard/Thống kê** | Chưa có tab dashboard — cần biểu đồ chi phí theo tháng, theo danh mục, so sánh tháng trước |
| 🔴 | **Attachment/Biên lai** | Chưa hỗ trợ upload ảnh biên lai/hoá đơn đính kèm từng chi phí |
| 🟡 | **Export báo cáo** | Chưa có tính năng export chi phí ra Excel/PDF theo tháng |
| 🟡 | **Auto-generate từ recurring** | Chi phí định kỳ chưa tự động tạo record mới mỗi tháng/tuần |
| 🟡 | **Budget/Ngân sách** | Chưa có tính năng đặt ngân sách cho từng danh mục và cảnh báo vượt ngân sách |
| 🟢 | **Phê duyệt chi phí** | Workflow phê duyệt chi phí (nhân viên → quản lý → kế toán) |
| 🟢 | **Liên kết với Invoice** | Link chi phí với hoá đơn để tính lợi nhuận ròng |

---

## 👷 3. Workforce App (Tốt nhưng thiếu báo cáo)

| Ưu tiên | Tính năng | Mô tả |
|---------|----------|-------|
| 🔴 | **Dashboard tổng quan** | Thiếu trang dashboard cho workforce — số freelancer active, tổng task, tổng chi phí, overdue tasks |
| 🟡 | **Báo cáo chi phí freelancer** | Chưa có báo cáo tổng chi phí workforce theo tháng/quý |
| 🟡 | **Export settlements** | Chưa có tính năng export bảng nghiệm thu ra Excel/PDF |
| 🟡 | **Task deadline & alerts** | Chưa có cảnh báo task quá hạn (overdue), nhắc nhở deadline sắp tới |
| 🟢 | **Timesheet** | Theo dõi số giờ làm việc của freelancer cho mỗi task |
| 🟢 | **Contract expiry alert** | Cảnh báo hợp đồng sắp hết hạn |

---

## 👥 4. CRM App (Cần bổ sung tương tác)

| Ưu tiên | Tính năng | Mô tả |
|---------|----------|-------|
| 🔴 | **Activity timeline / Ghi chú** | Chưa có lịch sử tương tác (gọi điện, email, meeting) cho mỗi khách hàng |
| 🔴 | **Pipeline / Sales funnel** | Chưa có Kanban board theo dõi khách hàng qua các giai đoạn (Lead → Qualified → Proposal → Won/Lost) |
| 🟡 | **Reminder / Follow-up** | Chưa có hệ thống nhắc việc follow-up cho sales |
| 🟡 | **Export khách hàng** | Chưa có tính năng export danh sách khách hàng ra Excel |
| 🟡 | **Linked Invoices** | Chưa liên kết khách hàng CRM ↔ hoá đơn Invoice — hiện tại 2 hệ thống khách hàng riêng rẽ (`invoice_clients` vs `crm_clients`) |
| 🟢 | **Email templates** | Gửi email marketing/follow-up cho khách hàng trực tiếp từ CRM |
| 🟢 | **Revenue per client** | Biểu đồ doanh thu theo khách hàng, tổng giá trị hợp đồng |

---

## 🧑‍💼 5. HR App (Cần cải thiện chi tiết nhân viên)

| Ưu tiên | Tính năng | Mô tả |
|---------|----------|-------|
| 🔴 | **Salary history chart** | Trang chi tiết nhân viên chưa hiển thị biến động lương theo thời gian |
| 🔴 | **Document upload** | DB có `hr_documents` nhưng chưa thấy UI quản lý tài liệu nhân viên (CMND, bằng cấp, hợp đồng scan) |
| 🟡 | **Evaluation/KPI** | DB có `hr_evaluations` (0 rows) nhưng chưa có UI cho đánh giá nhân viên — cần thêm trang đánh giá định kỳ |
| 🟡 | **Position history** | DB có `hr_position_history` (0 rows) nhưng chưa có UI ghi nhận lịch sử thăng chức/chuyển phòng |
| 🟡 | **Org chart** | Sơ đồ tổ chức trực quan (organization chart) theo phòng ban |
| 🟡 | **Dependent documents** | DB có `hr_dependent_documents` nhưng chưa có UI upload giấy tờ người phụ thuộc |
| 🟢 | **Onboarding checklist** | Danh sách các bước cần hoàn thành khi nhân viên mới vào |
| 🟢 | **Export nhân sự** | Export danh sách nhân viên ra Excel với thông tin lương |

---

## ⏰ 6. Chấm Công / Attendance (Cần kết nối mạnh hơn với Payroll)

| Ưu tiên | Tính năng | Mô tả |
|---------|----------|-------|
| 🔴 | **GPS/Location check-in** | Chưa có xác minh vị trí khi chấm công — hiện chỉ có manual check-in |
| 🔴 | **Overtime tracking** | Chưa theo dõi giờ OT tự động — Payroll cần dữ liệu OT nhưng hiện record chỉ có check_in/check_out |
| 🟡 | **Auto-calculate work hours** | Tính tổng giờ làm tự động từ check-in → check-out, so sánh với ca scheduled |
| 🟡 | **Bảng công chi tiết hơn** | Monthly sheet hiện chỉ nhập ngày công thủ công — cần tự tổng hợp từ records nếu có |
| 🟡 | **Calendar view** | Hiển thị lịch chấm công dạng calendar thay vì bảng, dễ nhìn hơn |
| 🟢 | **QR Code check-in** | DB có `att_qr_sessions` nhưng chưa thấy UI — triển khai chấm công QR thực tế |
| 🟢 | **Biometric / Face ID** | Tích hợp chấm công bằng nhận diện khuôn mặt (dài hạn) |

---

## 💵 7. Tính Lương / Payroll (Module mới nhất — cần hoàn thiện)

| Ưu tiên | Tính năng | Mô tả |
|---------|----------|-------|
| 🔴 | **Export bảng lương** | Chưa có tính năng export bảng lương ra Excel/PDF — rất cần cho kế toán |
| 🔴 | **Phiếu lương cá nhân** | Chưa có trang xem/in phiếu lương cho từng nhân viên (pay slip) |
| 🟡 | **Lịch sử lương** | Chưa có view so sánh bảng lương giữa các tháng |
| 🟡 | **Tự động lấy ngày công** | Hiện tính lương dựa trên monthly_records nhưng chưa auto-sync chặt chẽ với Attendance |
| 🟡 | **Thuế TNCN chi tiết** | Hiển thị bảng tính thuế TNCN từng bước rõ ràng hơn cho nhân viên |
| 🟢 | **Bank transfer file** | Xuất file chuyển khoản ngân hàng (format MB/VCB/ACB) để trả lương hàng loạt |
| 🟢 | **Payroll approval workflow** | Luồng phê duyệt: Kế toán tạo → Manager review → Giám đốc duyệt → Trả lương |

---

## 🌐 CẢI THIỆN TOÀN HỆ THỐNG (Cross-cutting)

### 🔐 Bảo mật & Phân quyền
| Ưu tiên | Vấn đề |
|---------|--------|
| 🔴 | **Auth chưa dùng Supabase Auth** — Login hiện check password trong table `invoice_accounts`, không hash password, không có session token thực sự |
| 🔴 | **Phân quyền theo app** — Hiện chỉ có `admin` vs `viewer`, chưa kiểm soát quyền truy cập từng module (ví dụ: nhân viên kế toán chỉ xem Invoice+Expense+Payroll) |
| 🟡 | **Audit log toàn hệ thống** — Chỉ Invoice có activity log, các module khác chưa ghi nhận ai làm gì khi nào |

### 📊 Dashboard & Analytics
| Ưu tiên | Vấn đề |
|---------|--------|
| 🔴 | **Home dashboard** — Trang HomeScreen chỉ hiện grid app cards, chưa có tổng quan: doanh thu tháng, chi phí tháng, số nhân viên, số task, v.v. |
| 🟡 | **Cross-module reports** — Chưa có báo cáo tổng hợp: Doanh thu - Chi phí = Lợi nhuận, chi phí workforce vs doanh thu, v.v. |

### 🔗 Tích hợp giữa các Module
| Ưu tiên | Vấn đề |
|---------|--------|
| 🔴 | **2 hệ thống khách hàng riêng rẽ** — `invoice_clients` (Invoice) và `crm_clients` (CRM) hoạt động độc lập, gây duplicate dữ liệu |
| 🟡 | **Attendance → Payroll** — Chấm công và tính lương chưa sync tự động chặt chẽ (ngày công, OT) |
| 🟡 | **HR → Workforce** — Freelancers quản lý riêng trong Workforce, full-time trong HR — có thể thống nhất |

### 🎨 UX & Performance
| Ưu tiên | Vấn đề |
|---------|--------|
| 🟡 | **Loading skeleton** — Nhiều trang chỉ hiện spinner đơn giản, chưa có skeleton loading |
| 🟡 | **Error boundary** — Chưa có React Error Boundary — lỗi 1 module có thể crash toàn app |
| 🟡 | **Keyboard shortcuts** — Chưa có hotkeys cho thao tác nhanh (Ctrl+S save, Ctrl+N new) |
| 🟢 | **Dark/Light toggle** — Chỉ Invoice có light mode, các app khác lock dark mode |
| 🟢 | **PWA / Offline** — Chưa hỗ trợ Progressive Web App — có thể dùng offline khi mất mạng |
| 🟢 | **Mobile responsive** — Một số bảng dữ liệu lớn chưa responsive tốt trên mobile |

### 📤 Xuất dữ liệu (Export)
| Ưu tiên | Vấn đề |
|---------|--------|
| 🔴 | **Chỉ Invoice có export** — 6 module còn lại đều chưa có tính năng export ra Excel/PDF |

---

## 🏆 Top 10 Tính Năng Nên Ưu Tiên Triển Khai

| # | Tính năng | Module | Lý do |
|---|----------|--------|-------|
| 1 | Export bảng lương (Excel/PDF) & Phiếu lương | Payroll | Kế toán cần ngay — module mới chưa dùng được nếu không export |
| 2 | Home Dashboard tổng quan | HomeScreen | Tạo giá trị ngay khi login — doanh thu, chi phí, nhân sự |
| 3 | Expense Dashboard + biểu đồ | Expense | Module hiện rất cơ bản, cần analytics |
| 4 | Thống nhất khách hàng Invoice ↔ CRM | Invoice + CRM | Tránh duplicate data, liên kết doanh thu với CRM |
| 5 | Upload biên lai/attachment cho Expense | Expense | Cần biên lai để phục vụ kế toán kiểm tra |
| 6 | Activity timeline cho CRM | CRM | CRM khi thiếu tương tác = chỉ là danh bạ |
| 7 | Export đa module (Excel/PDF) | All | Tất cả module cần export |
| 8 | OT tracking + Auto-sync Attendance → Payroll | Attendance + Payroll | Giảm nhập liệu thủ công, tăng chính xác |
| 9 | HR Document upload | HR | Đã có table nhưng chưa có UI |
| 10 | Phân quyền theo module | Platform | Bảo mật khi nhiều người dùng |
