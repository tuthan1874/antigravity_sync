# Employee Onboarding Flow

## Completed ✅
- [x] Quick Add Employee form (`QuickAddEmployee.tsx`) — simplified HR form
- [x] ⚡ Thêm nhanh button in `EmployeeList.tsx`
- [x] Tab routing in `HrApp.tsx` + `useHrState.ts`
- [x] Profile tab (`ProfileTab.tsx`) — employee self-service profile
- [x] `fetchMyProfile()` + `updateMyProfile()` in `portalService.ts`
- [x] "Hồ sơ" tab registered in `PortalApp.tsx`
- [x] Fix: ToastNotification props in PortalApp (wrong format)
- [x] Fix: Loading overlay for Quick Add submit (was freezing)
- [x] Fix: Missing `apikey` header in `create-employee-auth` call (401 error)

## TODO (tiếp ngày mai)
- [ ] Test invite email flow end-to-end after apikey fix
- [ ] Test Profile tab with a real linked employee account
- [ ] Verify password reset → profile completion flow
- [ ] Clean up test employees created during debugging (Test Invite User, etc.)
