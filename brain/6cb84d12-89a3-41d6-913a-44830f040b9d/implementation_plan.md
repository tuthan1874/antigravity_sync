# Freelancer Portal — Implementation Plan

Cho phép freelancer nhận invite qua email cá nhân, hoàn thiện hồ sơ và sử dụng portal riêng để xem task, nghiệm thu, và dashboard thu nhập.

## User Review Required

> [!IMPORTANT]
> **Liên kết dữ liệu:** Freelancer hiện tồn tại ở 2 bảng: `hr_employees` (hồ sơ HR) và `wf_workers` (workforce tasks/settlements). Plan này sẽ liên kết chúng qua trường `worker_id` mới trên `hr_employees`, đảm bảo freelancer đăng nhập bằng HR profile nhưng xem được data workforce.

> [!CAUTION]
> **Không động tới user hiện tại.** Mọi thay đổi edge function đều backward-compatible. Test bằng user mới tạo riêng.

## Proposed Changes

### 1. Auth & Role System

#### [MODIFY] [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts)
- Thêm role `'freelancer'` vào `AccountUser.role`
- Thêm `worker_id?: string` vào `AccountUser` (liên kết HR → Workforce)

#### [MODIFY] [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)
- Thêm `'freelancer'` vào `VALID_ROLES`
- Route `role === 'freelancer'` đến Freelancer Portal thay vì Employee Portal
- Profile completion cho freelancer dùng fields khác (không cần avatar, temp_address, insurance)
- Thêm `'freelancer-portal'` vào `VALID_APPS`

---

### 2. Invite Flow (HR → Freelancer)

#### [MODIFY] [hrService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/services/hrService.ts)
- Mở rộng `saveEmployee()`: khi `type === 'freelancer'` **cũng gửi invite** bằng email cá nhân (`email` thay vì `work_email`)
- Metadata gửi kèm: `{ role: 'freelancer', employee_id, worker_id }`

#### [MODIFY] Edge Function `create-employee-auth` (Supabase)
- Hỗ trợ nhận `role` param, set `role: 'freelancer'` vào user metadata
- Hỗ trợ nhận `worker_id` param để liên kết

#### [MODIFY] [EmployeeForm.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/components/EmployeeForm.tsx)
- Khi save freelancer với đủ: **Tên + Email + Chức danh + Chuyên môn** → auto-trigger invite
- Hiện trạng thái invite (✉️ Đã gửi invite / ⏳ Chờ hoàn thiện hồ sơ)

---

### 3. Profile Completion (Freelancer-specific)

#### [MODIFY] [ProfileCompletionScreen.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/ProfileCompletionScreen.tsx)
- Detect role từ user metadata
- **Freelancer required fields:** Họ tên, SĐT, Ngày sinh, Giới tính, Địa chỉ, CCCD (số/ngày cấp/nơi cấp), Ngân hàng (tên/STK/chủ TK), MST
- **Bỏ:** Avatar (optional cho FL), temp_address, insurance_number
- Tiêu đề hiện "Hoàn Thiện Hồ Sơ Cộng Tác Viên"

---

### 4. Freelancer Portal App

#### [NEW] [FreelancerPortalApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/freelancer-portal/components/FreelancerPortalApp.tsx)

**Tabs:**

| Tab | Nội dung |
|-----|----------|
| 📊 Dashboard | KPI cards (tổng task, tổng thu nhập, chưa thanh toán), biểu đồ thu nhập theo tháng |
| 📋 Tasks | Danh sách task được assign, filter theo status, xem chi tiết |
| 📑 Nghiệm thu | Danh sách phiếu nghiệm thu, xem chi tiết read-only |
| 👤 Hồ sơ | Xem/sửa thông tin cá nhân (reuse ProfileTab) |

**Gợi ý thêm:**
- 🔔 **Thông báo** — Badge trên tab Nghiệm thu khi có phiếu mới
- 📈 **Biểu đồ thu nhập** — Chart đơn giản (bar chart) thu nhập 6 tháng gần nhất
- 📋 **Hợp đồng** — Xem danh sách hợp đồng khoán việc đã ký

#### [NEW] [freelancerPortalService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/freelancer-portal/services/freelancerPortalService.ts)
- `fetchMyTasks(workerId)` — query `wf_tasks` theo `worker_id`
- `fetchMySettlements(workerId)` — query `wf_settlements` + `wf_settlement_tasks`
- `fetchDashboardStats(workerId)` — aggregate tasks/settlements cho KPI cards
- `fetchMyContracts(workerId)` — query `wf_contracts`

---

### 5. App Config & Routing

#### [MODIFY] [apps.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/config/apps.ts)
```ts
{
  id: 'freelancer-portal',
  name: 'Freelancer Portal',
  icon: '🎨',
  description: 'Tasks, nghiệm thu & thu nhập',
  color: '#F59E0B',
  gradient: 'linear-gradient(135deg, #F59E0B 0%, #D97706 100%)',
  roles: ['freelancer'],
}
```

#### [MODIFY] [HomeScreen.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/HomeScreen.tsx)
- Freelancer login → chỉ thấy 1 app "Freelancer Portal", auto-navigate

---

### 6. Database

#### Migration: `add_worker_id_to_hr_employees`
```sql
ALTER TABLE hr_employees ADD COLUMN worker_id UUID REFERENCES wf_workers(id);
```
Liên kết HR employee record với workforce worker record.

## Verification Plan

### Automated Tests
- Tạo **test freelancer mới** qua HR form (tên/email/chức danh/chuyên môn)
- Verify edge function gửi invite thành công
- Mở invite link → SetPassword → ProfileCompletion (freelancer fields)
- Login → HomeScreen chỉ hiện Freelancer Portal
- Portal: xem Dashboard stats, Tasks list, Settlements read-only, Profile edit
- Verify không ảnh hưởng user fulltime/parttime hiện tại

### Manual Verification
- Export PDF nghiệm thu vẫn hoạt động bình thường
- Kiểm tra RLS policies cho freelancer user chỉ xem được data của mình
