# Phase 2: Project Cleanup & Continued Optimization

## Goal
Continue database optimizations + clean up project structure by removing unused files, consolidating docs, and restructuring directories.

---

## Part A: Database — Remaining Optimizations

### A1. Optimize RLS policies — wrap `auth.uid()` in `(select ...)`
All existing RLS policies use `auth.uid()` directly, causing re-evaluation per row. Wrap them in `(select auth.uid())` for better performance at scale. **~35 policies** affected across tables: `accounts`, `journal_entries`, `departments`, `positions`, `company_settings`, `audit_logs`, `employees`, `employee_balances`, `employee_balance_transactions`, `balance_settings`, `expense_requests`, `notifications`, `employee_requests`, `user_2fa_factors`, `user_2fa_challenges`, `user_2fa_attempts`, `budget_categories`, `budget_allocations`.

### A2. Add RLS policies for 4 tables with RLS but no policies
- `employee_dependents` — employees can view own, admin/HR can manage all
- `financial_categories` — authenticated read, admin/accountant write
- `leave_balances` — employees can view own, admin/HR can manage all
- `salary_deductions` — employees can view own, admin/HR/accountant can manage all

---

## Part B: Project Cleanup

### B1. Delete unused/orphaned files

| File | Reason |
|------|--------|
| `lib/profile-completion-check-extended.ts` | Not imported anywhere |
| `components/api-test.tsx` | Not imported anywhere |
| `components/brainwave-interface.tsx` | Not imported anywhere |
| `check_roles.ps1` (1 byte, empty) | Unused empty file |
| `pnpm-lock.yaml` (96 bytes, stub) | Not using pnpm, npm is the package manager |
| `yarn.lock` (285KB) | Not using yarn, npm is the package manager |
| `update_roles.sql` | One-time script, belongs in database/ archive |
| `supabase-schema.sql` | Snapshot file, outdated, replaceable via Supabase |
| `supabase-schema-README.md` | Companion to the above |
| `database-mapping.md` | One-time reference, belongs in docs/ |
| `scripts/git-auto-pull.log` (1.5MB) | Log file, should not be in repo |

### B2. Consolidate root .md docs → `docs/` folder

Move 17 scattered .md files into `docs/`:

`ALLOWANCE_CALCULATION_LOGIC.md`, `ATTENDANCE_IMPORT_GUIDE.md`, `BUDGET_CODE_GENERATOR_GUIDE.md`, `BUDGET_INTEGRATION_GUIDE.md`, `CATEGORY_BUDGET_FEATURE.md`, `EMPLOYEE_TERMINATION_FEATURE.md`, `FINANCIAL_MANAGEMENT_ENHANCEMENT_REQUIREMENTS.md`, `FIX_BUDGET_CATEGORIES_ERROR.md`, `FIX_TRIGGER_ERROR.md`, `INTERN_PAYROLL_FEATURE.md`, `LEAVE_BALANCES_INTEGRATION.md`, `LEAVE_BALANCE_FEATURE.md`, `PAYROLL_CALCULATION_LOGIC.md`, `PAYROLL_LOGIC_2026_UPDATED.md`, `PROBATION_MANAGEMENT_FEATURE.md`, `README_2FA_SETUP.md`, `STORAGE_POLICIES_MANUAL_SETUP.md`, `TAX_TOGGLE_FEATURE.md`, `TRANSACTION_CATEGORY_SELECTOR_FEATURE.md`, `setup_budget_system_guide.md`

### B3. Archive database scripts → `database/archive/`

Move 60+ one-time SQL scripts into `database/archive/`. These are debug, fix, test, and setup scripts that were run once. Keep only `database/migrations/` clean.

### B4. Delete test/demo routes and data files

| Path | Reason |
|------|--------|
| `app/test/` (6 files) | Debug/test pages, not production |
| `app/budget-code-demo/` | Demo page |
| `app/api/debug/` | Debug API endpoint |
| `app/api/debug-2fa-secret/` | Debug API endpoint |
| `app/api/test-2fa/` | Test API endpoint |
| `app/api/test-2fa-complete/` | Test API endpoint |
| `app/api/test-r2/` | Test API endpoint |
| `app/api/test-totp/` | Test API endpoint |
| `data_import/` (CSV/XLSX files) | Raw import data, should not be in source |

### B5. Restructure `lib/` — split oversized files

#### [MODIFY] `lib/services.ts` (742 lines) → split into domain-specific service files
- `lib/services/employee-service.ts` — Employee CRUD + types
- `lib/services/department-service.ts` — Department CRUD + types
- `lib/services/position-service.ts` — Position CRUD + types
- `lib/services/attendance-service.ts` — Attendance calls + types
- `lib/services/payroll-service.ts` — Payroll calls + types
- `lib/services/notification-service-client.ts` — Client-side notification calls
- `lib/services/financial-service.ts` — Financial/budget calls + types
- `lib/services/index.ts` — Re-export barrel file (preserves import paths)

> [!IMPORTANT]
> The barrel file will re-export everything, so **existing imports** like `import { employeeService } from '@/lib/services'` will **continue to work** without changing any other files.

---

## Verification Plan
1. Run `npm run build` to verify no broken imports after file deletions and moves
2. Re-run Supabase **performance** and **security** advisors to confirm `auth_rls_initplan` warnings are resolved
