# TD Games Billing Platform — Tổng quan triển khai

## Kiến trúc tổng quan

| Thành phần | Công nghệ |
|---|---|
| Frontend | Vite + React 19 + TypeScript |
| Backend / DB | **Supabase** (project `Workflow` — `fifuhkupaqcfjwyouwpa`) |
| Auth | Custom login → RPC `invoice_verify_login` |
| Storage | Cloudflare R2 (tài liệu CRM) |
| Routing | Hash-based (`#invoice`, `#crm/payment`, …) |
| Deploy | VPS via GitHub Actions |

---

## 4 Module chính — Tất cả ✅ Hoàn thiện

### 1. 📄 Invoice — Quản lý hoá đơn & doanh thu

| Component | Chức năng |
|---|---|
| `InvoiceApp.tsx` | Shell + tab router |
| `InvoiceEditor.tsx` | Tạo/sửa hoá đơn |
| `InvoicePreview.tsx` | Xem trước & xuất PDF |
| `DashboardTab.tsx` | Thống kê doanh thu |
| `HistoryTab.tsx` | Lịch sử hoá đơn |
| `RecurringTab.tsx` | Hoá đơn định kỳ |
| `ActivityLogTab.tsx` | Nhật ký hoạt động |
| `FilterBar.tsx` | Bộ lọc |
| `Navbar.tsx` | Navigation + tỷ giá USD/VND |
| `EInvoiceModals.tsx` | Hoá đơn điện tử |
| `EmailModal.tsx` | Gửi email hoá đơn |

**Services:** `supabaseService.ts`, `exchangeRateService.ts`, `exportService.ts`, `sePayService.ts`

---

### 2. 💰 Expense — Quản lý chi phí

| Component | Chức năng |
|---|---|
| `ExpenseApp.tsx` | Shell + tab router |
| `ExpenseForm.tsx` | Thêm/sửa chi phí |
| `ExpenseList.tsx` | Danh sách chi phí |
| `ExpenseCategoryManager.tsx` | Quản lý danh mục |
| `ExpenseRecurring.tsx` | Chi phí định kỳ |

**Services:** `expenseService.ts`

---

### 3. 👷 Workforce — Quản lý nhân sự & nghiệm thu

| Component | Chức năng |
|---|---|
| `WorkforceApp.tsx` | Shell + tab router |
| `WorkerList.tsx` | Danh sách nhân sự |
| `WorkerForm.tsx` | Thêm/sửa nhân sự |
| `TaskList.tsx` | Danh sách task (sync ClickUp) |
| `SettlementManager.tsx` | Nghiệm thu & thanh toán |
| `ClickUpConfig.tsx` | Cấu hình ClickUp sync |

**Services:** `workforceService.ts`, `clickupService.ts`

---

### 4. 👥 CRM — Quản lý khách hàng

| Component | Chức năng |
|---|---|
| `CrmApp.tsx` | Shell + tab router |
| `ClientList.tsx` | Danh sách khách hàng |
| `ClientForm.tsx` | Thêm/sửa khách hàng |
| `ProjectList.tsx` | Dự án theo khách hàng |
| `DocumentList.tsx` | Tài liệu (Cloudflare R2) |
| `PaymentTracker.tsx` | Theo dõi thanh toán |

**Services:** `crmService.ts`

---

## Supabase Database — 17 bảng

| Bảng | Module | Rows |
|---|---|---|
| `invoice_invoices` | Invoice | 5 |
| `invoice_banks` | Invoice | 2 |
| `invoice_clients` | Invoice | 2 |
| `invoice_studios` | Invoice | 2 |
| `invoice_accounts` | Auth | 2 |
| `invoice_activity_logs` | Invoice | 7 |
| `invoice_recurring` | Invoice | 0 |
| `expense_categories` | Expense | 7 |
| `expense_expenses` | Expense | 0 |
| `expense_recurring` | Expense | 0 |
| `wf_workers` | Workforce | 3 |
| `wf_contracts` | Workforce | 0 |
| `wf_tasks` | Workforce | 21 |
| `wf_settlements` | Workforce | 0 |
| `wf_settlement_tasks` | Workforce | 0 |
| `wf_clickup_config` | Workforce | 1 |
| `crm_clients` | CRM | 3 |
| `crm_contacts` | CRM | 2 |
| `crm_documents` | CRM | 1 |
| `crm_projects` | CRM | 1 |
| `crm_project_files` | CRM | 0 |

> Tất cả bảng đều bật **RLS** (Row Level Security).

---

## Shared Components

| Component | Chức năng |
|---|---|
| `LoginScreen.tsx` | Đăng nhập |
| `HomeScreen.tsx` | Trang chủ — chọn module |
| `Button.tsx` | Button tái sử dụng |
| `FormElements.tsx` | Input, Select, Label |
| `ToastNotification.tsx` | Thông báo toast |

---

## Các tính năng đã triển khai gần đây

| Thời gian | Tính năng |
|---|---|
| 15/03 | CRM Payment View — hiển thị tất cả hoá đơn mặc định |
| 15/03 | Fix R2 Public URL — preview/download file từ Cloudflare R2 |
| 14/03 | Fix Worker Delete — xoá nhân sự + cascade data |
| 13/03 | Tỷ giá USD/VND — hiển thị trên Navbar |
| 12/03 | PDF Export — edge function |
| 12/03 | Fix Sync Config Cascade |
| 11/03 | Debug Invoice Deploy — fix deployment VPS |
| 10/03 | Improve Invoice UI/UX — chỉ tính task có Closed_Date |

---

## Tóm tắt

> **Tất cả 4 module đã hoàn thiện.** 40 component files, 17 bảng Supabase, backend 100% Supabase (project `Workflow`). Dự án đang ở phase **bảo trì + cải tiến**.
