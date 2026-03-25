# Freelancer Portal — Tasks

## 1. Auth & Role System
- [x] Add `'freelancer'` role to `AccountUser` in `types.ts`
- [x] Add `worker_id` to `AccountUser`
- [x] Update `VALID_ROLES` in `App.tsx`
- [x] Route freelancer to FreelancerPortal

## 2. Database
- [ ] Migration: add `worker_id` to `hr_employees` (Supabase access limited — manual)

## 3. Invite Flow
- [x] Update `hrService.saveEmployee()` to invite freelancers via personal email
- [ ] Deploy updated edge function `create-employee-auth` (saved locally, needs deploy)
- [x] EmployeeForm already shows invite status for freelancers

## 4. Profile Completion
- [x] Make `ProfileCompletionScreen` role-aware with freelancer-specific fields

## 5. Freelancer Portal App
- [x] Create `freelancerPortalService.ts`
- [x] Create `FreelancerPortalApp.tsx` with Dashboard, Tasks, Settlements, Profile tabs

## 6. App Config & Routing
- [x] Add freelancer-portal to `apps.ts`
- [x] Update `App.tsx` routing for freelancer-portal
- [x] Auto-navigate freelancer to portal on login

## 7. Quick Add Freelancer
- [x] Add mode toggle (Nhân viên / Freelancer) to QuickAddEmployee
- [x] Simplified freelancer form: name, email, specializations, level

## 8. Email Safety & Auth Cleanup
- [x] Cross-check email between fulltime `work_email` and freelancer `email`
- [x] Auto-delete Auth user on HR employee deletion
- [x] Edge function: add `delete` and `check_email` actions
- [ ] **Deploy edge function** `create-employee-auth` (manual deploy required)

## 9. Verification
- [x] Vite production build passes
- [ ] Deploy edge function & run DB migration
- [ ] Test full flow: create → cross-check → delete → verify auth cleanup
