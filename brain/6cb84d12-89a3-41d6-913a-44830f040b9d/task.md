# Freelancer Portal — Tasks

## 1. Auth & Role System
- [x] Add `'freelancer'` role to `AccountUser` in `types.ts`
- [x] Add `worker_id` to `AccountUser`
- [x] Update `VALID_ROLES` in `App.tsx`
- [x] Route freelancer to FreelancerPortal

## 2. Database
- [x] Migration: `worker_id` on `hr_employees`
- [x] Migration: CASCADE delete FK constraints

## 3. Invite Flow
- [x] Update `hrService.saveEmployee()` to invite freelancers via personal email
- [x] Deploy edge function `create-employee-auth` v8

## 4. Profile Completion
- [x] Make `ProfileCompletionScreen` role-aware

## 5. Freelancer Portal App
- [x] `freelancerPortalService.ts`
- [x] `FreelancerPortalApp.tsx` (Dashboard, Tasks, Settlements, Profile)

## 6. App Config & Routing
- [x] Add freelancer-portal to `apps.ts`
- [x] Update `App.tsx` routing

## 7. Quick Add Freelancer
- [x] Mode toggle (Nhân viên / Freelancer)
- [x] Simplified freelancer form

## 8. Email Safety & Auth Management
- [x] Cross-check email (fulltime work_email ↔ freelancer email)
- [x] Soft delete (status='terminated' + Auth ban)
- [x] `reactivateEmployee()` + Auth unban
- [x] Edge function: `disable`, `enable`, `check_email` actions
- [x] Deployed edge function v8

## 9. Git
- [x] Committed & pushed to `tdgamesvn/tdgames_billing` (main: 0bc4aef)

## 10. Pending
- [ ] Thêm nút "Kích hoạt lại" trên UI cho nhân sự terminated
- [ ] Test soft delete + reactivate end-to-end
- [ ] Verify invite email qua Resend logs
- [ ] Test freelancer full login flow
