# Freelancer Portal & HR Enhancements — Walkthrough

## Tổng quan
Triển khai hệ thống **Freelancer Portal** tích hợp vào app HR hiện tại, bao gồm onboarding, quản lý task, nghiệm thu, và các cải tiến bảo mật cho việc quản lý nhân sự.

## Các tính năng đã triển khai

### 1. Freelancer Portal
- Portal riêng (`FreelancerPortalApp.tsx`) với theme amber
- 4 tab: Dashboard, Tasks, Settlements, Profile
- Service layer (`freelancerPortalService.ts`)

### 2. HR Quick Add — Freelancer Mode
- Toggle **Nhân viên / Freelancer** trong Quick Add
- Freelancer chỉ cần 4 trường: Tên, Email, Chuyên môn, Level
- Tự động gửi invite email qua Resend

### 3. Cross-check Email
- Kiểm tra chéo `work_email` (fulltime) và `email` (freelancer)
- Ngăn conflict khi cùng email dùng cho cả 2 loại nhân sự
- Hàm `checkEmailConflict()` trong `hrService.ts`

### 4. Soft Delete
- **Trước**: Hard delete → mất hết dữ liệu lịch sử
- **Sau**: `status = 'terminated'` → giữ nguyên payroll, attendance, contracts
- Auth user bị **ban** (không xoá), có thể **kích hoạt lại**
- Hàm `reactivateEmployee()` để khôi phục nhân sự

### 5. Edge Function `create-employee-auth` (v8)
4 actions: `invite` (default), `disable` (ban), `enable` (unban), `check_email`

### 6. DB Migration
- `cascade_delete_hr_employees`: FK constraints → ON DELETE CASCADE
- `hr_employees.worker_id` → FK tới `wf_workers`

## Files đã sửa
| File | Thay đổi |
|---|---|
| `hrService.ts` | `checkEmailConflict`, `deleteEmployee` (soft), `reactivateEmployee`, `disableAuthUser`, `enableAuthUser` |
| `useHrState.ts` | `handleDeleteEmployee` (soft), `handleReactivateEmployee` |
| `QuickAddEmployee.tsx` | Freelancer mode toggle, cross-check email |
| `create-employee-auth/index.ts` | `disable`, `enable`, `check_email` actions |
| `FreelancerPortalApp.tsx` | New portal app |
| `freelancerPortalService.ts` | New service layer |
| `ProfileCompletionScreen.tsx` | Role-aware (freelancer fields) |
| `App.tsx` | Freelancer routing |
| `apps.ts` | Freelancer portal config |
| `types.ts` | `freelancer` role, `worker_id` |

## Pending / Next Steps
- [ ] Test soft delete flow end-to-end trên production
- [ ] Thêm nút "Kích hoạt lại" trên UI cho nhân sự terminated
- [ ] Verify invite email delivery qua Resend logs
- [ ] Test freelancer login flow hoàn chỉnh
