# Employee Onboarding Flow

## 1. Planning
- [x] Research existing codebase (HR module, Portal, Auth, Types)
- [x] Write implementation plan
- [x] Get user approval

## 2. Quick Add Employee (HR Side)
- [x] Create `QuickAddEmployee.tsx` — simplified form with only onboarding fields
- [x] Add "⚡ Thêm nhanh" button in `EmployeeList.tsx` alongside existing "Add"
- [x] Wire up Quick Add in `HrApp.tsx` as new tab/view
- [x] Ensure `saveEmployee()` auto-invite flow works (already exists)

## 3. Employee Profile Tab (Portal Side)
- [x] Add `fetchMyProfile()` and `updateMyProfile()` to `portalService.ts`
- [x] Create `ProfileTab.tsx` — employee self-service profile view/edit
  - [x] Read-only for HR-set fields
  - [x] Editable for personal fields
  - [x] Profile completion progress indicator
  - [x] Photo upload support
- [x] Register `ProfileTab` in `PortalApp.tsx` as "Hồ sơ" tab

## 4. Verification
- [x] Test HR Quick Add flow in browser — ✅ passes
- [x] Test Portal Profile tab in browser — ✅ passes
