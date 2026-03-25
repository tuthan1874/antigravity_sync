# Freelancer Portal — Tasks

## 1. Auth & Role System
- [ ] Add `'freelancer'` role to `AccountUser` in `types.ts`
- [ ] Add `worker_id` to `AccountUser`
- [ ] Update `VALID_ROLES` in `App.tsx`
- [ ] Route freelancer to FreelancerPortal

## 2. Database
- [ ] Migration: add `worker_id` to `hr_employees`

## 3. Invite Flow
- [ ] Update `hrService.saveEmployee()` to invite freelancers via personal email
- [ ] Update edge function `create-employee-auth` to support freelancer role
- [ ] Update `EmployeeForm.tsx` to show invite status for freelancers

## 4. Profile Completion
- [ ] Make `ProfileCompletionScreen` role-aware with freelancer-specific fields

## 5. Freelancer Portal App
- [ ] Create `freelancerPortalService.ts` (fetchMyTasks, fetchMySettlements, fetchDashboardStats, fetchMyContracts)
- [ ] Create `FreelancerPortalApp.tsx` with Dashboard, Tasks, Settlements, Profile tabs
- [ ] Dashboard tab with KPI cards and income chart
- [ ] Tasks tab with task list and status filters
- [ ] Settlements tab with read-only settlement detail view
- [ ] Profile tab (reuse ProfileTab)

## 6. App Config & Routing
- [ ] Add freelancer-portal to `apps.ts`
- [ ] Update `App.tsx` routing for freelancer-portal
- [ ] Auto-navigate freelancer to portal on login

## 7. Verification
- [ ] Create test freelancer user
- [ ] Test full flow: invite → set password → profile → portal
- [ ] Verify existing users not affected
