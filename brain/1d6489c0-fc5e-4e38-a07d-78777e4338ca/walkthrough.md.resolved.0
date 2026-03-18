# TD Games Billing App — Trạng Thái Triển Khai

> **Dev server:** `http://localhost:3000/` (Vite v6.4.1)
> **Database:** Supabase project `Workflow` (`fifuhkupaqcfjwyouwpa`) — region: `ap-northeast-1`

---

## Tổng Quan: 7 Module Đã Triển Khai

| # | Module | Trạng thái | DB Tables | Dữ liệu thực |
|---|--------|-----------|-----------|--------------|
| 1 | 📄 **Invoice** | ✅ Hoàn thiện | 6 tables | 5 invoices, 2 studios, 2 banks, 2 clients |
| 2 | 💰 **Expense** | ✅ Hoàn thiện | 3 tables | 7 categories, 0 expenses |
| 3 | 👷 **Workforce** | ✅ Hoàn thiện | 6 tables | 3 workers, 31 tasks, 1 ClickUp config |
| 4 | 👥 **CRM** | ✅ Hoàn thiện | 5 tables | 3 clients, 2 contacts, 1 project, 1 doc |
| 5 | 🧑‍💼 **HR** | ✅ Hoàn thiện | 11 tables | 4 employees, 9 departments, 6 salary components |
| 6 | ⏰ **Chấm Công** | ✅ Hoàn thiện | 6 tables | 1 shift, 1 monthly sheet |
| 7 | 💵 **Tính Lương** | ✅ Hoàn thiện | 2 tables | 0 records (chưa tạo bảng lương) |

---

## Chi Tiết Từng Module

### 1. 📄 Invoice
- **5 tabs**: Editor, History, Dashboard, Activity Log, Recurring
- **Tính năng**: Tạo/sửa/xoá hoá đơn, eInvoice qua SePay, export PDF, gửi email, tỷ giá VCB live, chuyển đổi USD→VND
- **DB**: `invoice_invoices` (5), `invoice_studios` (2), `invoice_banks` (2), `invoice_clients` (2), `invoice_accounts` (2), `invoice_activity_logs` (7), `invoice_recurring` (0)

### 2. 💰 Expense
- **3 tabs**: Danh sách, Định kỳ, Danh mục
- **Tính năng**: CRUD chi phí, chi phí định kỳ, quản lý danh mục, lọc theo trạng thái/ngày/loại
- **DB**: `expense_categories` (7), `expense_expenses` (0), `expense_recurring` (0)

### 3. 👷 Workforce
- **5 tabs**: Nhân sự, Thêm/Sửa, Task, Nghiệm thu, Cấu hình ClickUp
- **Tính năng**: Quản lý freelancer, sync tasks từ ClickUp, settlements/nghiệm thu, hợp đồng
- **DB**: `wf_workers` (3), `wf_tasks` (31), `wf_contracts` (0), `wf_settlements` (0), `wf_settlement_tasks` (0), `wf_clickup_config` (1)

### 4. 👥 CRM
- **5 tabs**: Khách hàng, Dự án, Tài liệu, Thanh toán, Thống kê
- **Tính năng**: CRUD khách hàng + contacts, upload tài liệu lên R2, theo dõi thanh toán, biểu đồ thống kê
- **DB**: `crm_clients` (3), `crm_contacts` (2), `crm_projects` (1), `crm_documents` (1), `crm_project_files` (0)

### 5. 🧑‍💼 HR
- **4 tabs**: Nhân sự, Phòng ban, Nhắc việc (+ Chi tiết & Form nhân viên)
- **Tính năng**: Quản lý nhân viên toàn diện, phòng ban, hợp đồng, lương cơ bản, người phụ thuộc, nhắc nhở tự động
- **DB**: `hr_employees` (4), `hr_departments` (9), `hr_contracts` (0), `hr_salary_components` (6), `hr_employee_salary` (6), `hr_dependents` (1), `hr_dependent_documents` (0), `hr_position_history` (0), `hr_evaluations` (0), `hr_project_history` (0), `hr_documents` (0), `hr_reminders` (0)

### 6. ⏰ Chấm Công (Attendance)
- **5 tabs**: Dashboard, Bảng công, Ca làm việc, Đơn từ, Báo cáo
- **Tính năng**: Check-in/out, quản lý ca, bảng công tháng (nhập công thủ công), đơn nghỉ phép, báo cáo
- **DB**: `att_shifts` (1), `att_employee_shifts` (1), `att_records` (0), `att_requests` (0), `att_qr_sessions` (0), `att_monthly_sheets` (1), `att_monthly_records` (1)

### 7. 💵 Tính Lương (Payroll)
- **1 tab**: Bảng lương (List → Detail)
- **Tính năng**: Tạo bảng lương tháng, tính lương 8 bước (gross → net), BHXH/BHYT/BHTN, thuế TNCN, xác nhận bảng lương
- **DB**: `pay_payroll_sheets` (0), `pay_payroll_records` (0)

---

## Hạ Tầng Chung

| Thành phần | Trạng thái |
|-----------|-----------|
| 🔐 Login/Auth | ✅ Local auth + localStorage (30-day session) |
| 🎨 Dark Theme | ✅ Toàn bộ app (glassmorphism, glow blobs, grid) |
| 🧭 Hash Router | ✅ `#app/tab` format, back/forward support |
| 💱 VCB Exchange Rate | ✅ Live trong navbar (Invoice, Expense, Workforce) |
| ☁️ Cloudflare R2 | ✅ File storage cho CRM documents |
| 📧 SePay eInvoice | ✅ Tích hợp qua Edge Function proxy |
| 🔔 Toast Notifications | ✅ Toàn bộ app |
| 📱 Responsive | ✅ Mobile-friendly layouts |

---

## Tổng Kết

**Tất cả 7 module đã được triển khai đầy đủ** về mặt code (components, hooks, services). Database đã có schema hoàn chỉnh với 58 tables trên Supabase. Một số module đã có dữ liệu thực (Invoice, Workforce, CRM, HR, Attendance), trong khi Expense và Payroll chưa có dữ liệu sử dụng.
