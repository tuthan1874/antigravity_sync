# Bổ sung Cấu trúc lương vào HR

## Database
- [x] Migration: tạo `hr_salary_components` + `hr_employee_salary` + RLS + seed data

## TypeScript Types
- [x] Thêm `HrSalaryComponent` + `HrEmployeeSalary` vào `types.ts`

## Service Layer
- [x] Thêm CRUD functions vào `hrService.ts`

## UI Components
- [x] `SalaryComponentManager.tsx` — admin quản lý khoản lương mẫu
- [x] Thêm tab "Cấu trúc lương" vào `HrApp.tsx` + `useHrState.ts`
- [x] Thêm sub-tab "💰 Cấu trúc lương" vào `EmployeeDetail.tsx`

## Verification
- [/] Browser test: CRUD khoản lương + gán cho nhân viên
