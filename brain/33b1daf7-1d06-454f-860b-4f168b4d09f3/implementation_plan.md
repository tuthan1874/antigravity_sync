# HR Management App — Implementation Plan

Xây dựng module quản lý nhân sự toàn diện cho TD Games Platform, hỗ trợ cả fulltime và freelancer. Module này sẽ là **nguồn dữ liệu nhân sự trung tâm** cho toàn bộ hệ sinh thái app.

## User Review Required

> [!IMPORTANT]
> **Tích hợp với Workforce:** Module Workforce hiện quản lý nhân sự qua bảng `wf_workers`. Sau khi HR App hoàn thành, Workforce sẽ cần chuyển sang đọc dữ liệu từ `hr_employees`. Đề xuất triển khai HR App trước, tích hợp sau để tránh phá vỡ Workforce hiện tại.

> [!WARNING]
> **Migration dữ liệu:** 3 workers hiện tại trong `wf_workers` sẽ cần migrate sang `hr_employees`. Plan này sẽ xử lý migration sau khi HR App stable.

---

## Proposed Changes

### Database — Supabase Migration

Tạo 8 bảng mới trong Supabase project `Workflow` (`fifuhkupaqcfjwyouwpa`):

#### `hr_employees` — Bảng chính, lưu thông tin nhân sự

```sql
-- Thông tin chung (cả fulltime + freelancer)
id              uuid PK DEFAULT gen_random_uuid()
employee_code   text UNIQUE          -- Mã nhân sự tự sinh: FT-001, FL-001
type            text NOT NULL         -- 'fulltime' | 'freelancer' | 'parttime'
status          text DEFAULT 'active' -- 'active' | 'inactive' | 'offboarded' | 'blacklist'
full_name       text NOT NULL
avatar_url      text
email           text
phone           text
date_of_birth   date
gender          text                  -- 'male' | 'female' | 'other'
nationality     text DEFAULT 'Vietnam'
address         text

-- Fulltime-specific
id_number       text      -- CMND/CCCD
id_issue_date   date
id_issue_place  text
tax_code        text      -- MST cá nhân
insurance_number text     -- Số sổ bảo hiểm
department_id   uuid FK → hr_departments
position        text      -- Chức danh
level           text      -- Junior/Mid/Senior/Lead/Manager
salary          numeric
salary_currency text DEFAULT 'VND'
start_date      date      -- Ngày bắt đầu làm việc
probation_end   date      -- Ngày hết thử việc

-- Freelancer-specific
portfolio_url   text
specializations text[]    -- ['2D', '3D', 'VFX', 'Concept Art', ...]
timezone        text      -- 'UTC+7', 'UTC+9'...
rate_type       text      -- 'hourly' | 'per_shot' | 'per_deliverable' | 'per_task'
rate_amount     numeric
rate_currency   text DEFAULT 'USD'
payment_method  text      -- 'bank_transfer' | 'paypal' | 'wise' | 'other'
payment_details jsonb     -- { paypal_email, wise_id, etc. }

-- Banking (shared)
bank_name       text
bank_account    text
bank_branch     text

-- Meta
notes           text
tags            text[]
created_at      timestamptz DEFAULT now()
updated_at      timestamptz DEFAULT now()
```

#### `hr_departments` — Phòng ban

```
id, name, code, description, manager_id (FK → hr_employees), is_active, created_at
```

Seed data: Art, Animation, VFX, R&D, Production, Management, HR, Finance

#### `hr_contracts` — Hợp đồng

```
id, employee_id (FK), contract_type ('labor'|'service'|'nda'|'appendix'),
title, contract_number, start_date, end_date,
salary, currency, rate_type, rate_amount,
file_url, status ('active'|'expired'|'terminated'),
notes, created_at
```

#### `hr_position_history` — Lịch sử thay đổi

```
id, employee_id (FK), change_type ('position'|'department'|'salary'|'level'),
old_value, new_value, effective_date, reason, created_at
```

#### `hr_evaluations` — Đánh giá năng lực

```
id, employee_id (FK), period (text: 'Q1-2026'),
evaluator, score (1-5), strengths, weaknesses, notes,
next_evaluation_date, status ('pending'|'completed'), created_at
```

#### `hr_project_history` — Lịch sử dự án

```
id, employee_id (FK), project_name, role, start_date, end_date,
performance_note, created_at
```

#### `hr_documents` — Tài liệu số hóa

```
id, employee_id (FK), doc_type ('id_card'|'contract'|'diploma'|'certificate'|'other'),
title, file_url, file_name, file_size, notes, created_at
```

#### `hr_reminders` — Nhắc nhở

```
id, employee_id (FK), type ('contract_expiry'|'birthday'|'evaluation'|
  'work_permit'|'freelancer_payment'|'probation_end'|'anniversary'),
title, due_date, status ('pending'|'notified'|'dismissed'),
notes, created_at
```

---

### Frontend — New Files

#### [NEW] [hrService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/services/hrService.ts)

Supabase CRUD service cho tất cả 8 bảng. Theo pattern của `workforceService.ts` / `crmService.ts`.

Các function chính:
- `fetchEmployees()`, `saveEmployee()`, `updateEmployee()`, `deleteEmployee()`
- `fetchDepartments()`, `saveDepartment()`, `updateDepartment()`, `deleteDepartment()`
- `fetchContracts(employeeId)`, `saveContract()`, `updateContract()`, `deleteContract()`
- `fetchPositionHistory(employeeId)`, `addPositionChange()`
- `fetchEvaluations(employeeId)`, `saveEvaluation()`, `updateEvaluation()`
- `fetchProjectHistory(employeeId)`
- `fetchDocuments(employeeId)`, `uploadDocument()`, `deleteDocument()`
- `fetchReminders()`, `generateReminders()`, `dismissReminder()`

---

#### [NEW] [useHrState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/hooks/useHrState.ts)

Custom hook quản lý state toàn bộ HR module. Theo pattern của `useWorkforceState.ts`.

Tabs: `employees` | `employeeForm` | `departments` | `reminders`

State: employees, departments, contracts, filters (type, status, department, search), editing state, toast.

---

#### [NEW] [HrApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/HrApp.tsx)

Shell component + tab router. Reuse shared `Navbar`. 4 tabs chính:
- **Nhân sự** — Danh sách + tìm kiếm/lọc
- **Hồ sơ** — Thêm/sửa/xem chi tiết
- **Phòng ban** — Quản lý departments
- **Nhắc việc** — Dashboard cảnh báo

---

#### [NEW] [EmployeeList.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeList.tsx)

Danh sách nhân sự với:
- Summary cards (tổng, fulltime, freelancer, active, inactive)
- Search bar (tìm theo tên, email, mã NV)
- Filters: loại (fulltime/freelancer/parttime), trạng thái, phòng ban, chuyên môn
- Card view (tương tự WorkerList nhưng chi tiết hơn)
- Quick actions: xem chi tiết, sửa, toggle active, xóa

---

#### [NEW] [EmployeeForm.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeForm.tsx)

Form nhập liệu phân chia theo section:
- **Thông tin cá nhân** — Tên, email, SĐT, ngày sinh, giới tính, quốc tịch, ảnh
- **Fulltime fields** — (conditional) CCCD, MST, bảo hiểm, phòng ban, chức vụ, lương
- **Freelancer fields** — (conditional) Portfolio, chuyên môn, rate card, timezone, payment method
- **Ngân hàng** — Bank info
- **Hợp đồng** — (khi editing) Danh sách hợp đồng + thêm mới
- **Lịch sử** — (khi editing) Position changes, evaluations, project history

---

#### [NEW] [EmployeeDetail.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeDetail.tsx)

Trang chi tiết hồ sơ nhân viên (read-only view + inline edit):
- Header card: avatar, tên, mã NV, type badge, status
- Tabs con: Thông tin | Hợp đồng | Lịch sử | Đánh giá | Dự án | Tài liệu
- Timeline view cho lịch sử thay đổi

---

#### [NEW] [DepartmentManager.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/DepartmentManager.tsx)

Quản lý phòng ban:
- CRUD phòng ban
- Xem số nhân sự trong mỗi phòng ban
- Chọn manager cho mỗi phòng ban

---

#### [NEW] [ReminderDashboard.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/ReminderDashboard.tsx)

Dashboard cảnh báo:
- Auto-generate reminders (hợp đồng hết hạn 30/15/7 ngày, sinh nhật, evaluation đến hạn, v.v.)
- Filter theo loại, theo thời gian
- Mark as dismissed
- Color-coded urgency (red: ≤7 days, orange: ≤15 days, yellow: ≤30 days)

---

### App Registration

#### [MODIFY] [apps.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/config/apps.ts)

Thêm entry cho HR app:

```diff
+  {
+    id: 'hr',
+    name: 'HR',
+    icon: '🧑‍💼',
+    description: 'Quản lý nhân sự toàn diện',
+    color: '#FF375F',
+    gradient: 'linear-gradient(135deg, #FF375F 0%, #FF6B81 100%)',
+  },
```

#### [MODIFY] [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)

```diff
+import HrApp from './apps/hr/components/HrApp';
 const VALID_APPS = ['invoice', 'expense', 'workforce', 'crm'];
+const VALID_APPS = ['invoice', 'expense', 'workforce', 'crm', 'hr'];
 ...
+  if (activeApp === 'hr') {
+    return <HrApp currentUser={currentUser} onBack={handleBack} initialTab={initialTab} />;
+  }
```

#### [MODIFY] [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts)

Thêm các type definitions cho HR module: `HrEmployee`, `HrDepartment`, `HrContract`, `HrPositionHistory`, `HrEvaluation`, `HrProjectHistory`, `HrDocument`, `HrReminder`.

---

## Verification Plan

### Browser Tests

Không có unit tests trong project hiện tại (Vite dev server only, không có test framework). Toàn bộ verification sẽ thông qua browser testing:

1. **Chạy dev server:** `npm run dev` → http://localhost:3000
2. **Kiểm tra Home Screen:**  
   - Đăng nhập → Confirm thấy card "HR" mới trên trang chủ → Click vào để mở
3. **Tab Nhân sự — CRUD:**  
   - Thêm 1 nhân sự fulltime (điền đầy đủ CCCD, phòng ban, lương)
   - Thêm 1 nhân sự freelancer (điền portfolio, chuyên môn, rate card)
   - Verify danh sách hiển thị đúng, filter theo loại/trạng thái hoạt động
   - Sửa thông tin → Verify cập nhật đúng
   - Xóa → Verify đã xóa
4. **Tab Phòng ban:**  
   - Kiểm tra seed data hiển thị (Art, Animation, VFX, …)
   - Thêm/sửa/xóa phòng ban
5. **Chi tiết nhân viên:**  
   - Click vào nhân viên → Verify hiển thị đầy đủ thông tin
   - Thêm hợp đồng → Verify hiện trong tab Hợp đồng
   - Thêm đánh giá → Verify hiện trong tab Đánh giá
6. **Tab Nhắc việc:**  
   - Tạo nhân sự có hợp đồng hết hạn trong 15 ngày tới
   - Verify reminder được tự động tạo và hiển thị đúng màu urgency
   - Dismiss reminder → Verify đã ẩn
7. **Build check:** `npm run build` — verify không có lỗi TypeScript
