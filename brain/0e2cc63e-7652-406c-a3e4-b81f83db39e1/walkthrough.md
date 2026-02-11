# HRM Backend Optimization — Final Walkthrough

## Phase 1: JWT Custom Claims ✅

| Migration | Changes |
|-----------|---------|
| `create_custom_access_token_hook` | Hook injects `user_role` + `employee_id` into JWT. Refactored `current_user_role()` and `current_user_employee_id()` to read from JWT |

> [!IMPORTANT]
> **Manual step:** Enable hook on [Dashboard → Auth → Hooks](https://supabase.com/dashboard/project/hbzgoguwpayuhvbvinqy/auth/hooks) → Custom Access Token → `public.custom_access_token_hook`

---

## Phase 2: Indexing & Integrity ✅

| Migration | Changes |
|-----------|---------|
| `drop_duplicate_indexes_v2` | Dropped 11 redundant indexes/constraints |
| `add_employees_lead_id_fkey` | Added FK constraint `employees.lead_id → employees.id` |
| `refactor_get_managed_employee_ids_v2` | Added `(select ...)` wrapper for RLS best practice |

---

## Phase 3: Security Hardening ✅

| Migration | Changes |
|-----------|---------|
| `fix_using_true_policies` | Fixed 2 `using(true)` policies → now require `authenticated` |
| `rewrite_role_check_subquery_policies` | Rewrote 13 policies: `EXISTS(SELECT FROM employees...)` → `current_user_role()` |
| `rewrite_employee_id_subquery_policies` | Rewrote 11 policies: `employee_id IN (SELECT...)` → `current_user_employee_id()` + 3 complex notification policies |
| `fix_function_search_path` | Set `search_path = ''` on all 4 helper functions (security advisor fix) |

### Verification Results

| Test | Result |
|------|--------|
| No `using(true)` for public roles | ✅ Empty |
| No raw subqueries to `employees` in policies | ✅ Empty |
| Total policy count | ✅ 73 policies |
| Function search_path warnings | ✅ Fixed |

### Remaining Security Advisor Warnings (non-RLS)

| Warning | Action Required |
|---------|----------------|
| Auth OTP long expiry | Consider reducing OTP expiry to < 1 hour |
| Leaked password protection disabled | Consider enabling in Auth settings |
| Postgres version has security patches | Consider upgrading Postgres |
