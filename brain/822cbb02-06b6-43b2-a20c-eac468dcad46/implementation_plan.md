# Implementation Plan - Database Optimization

## Goal Description
Optimize the HRM database by adding missing indexes to Foreign Key columns. This will improve the performance of `JOIN` queries and data retrieval, especially for relationships between employees, departments, and financial transactions.

## User Review Required
> [!IMPORTANT]
> This change involves creating a new migration file. Please confirm if you want me to generate this migration file in `source/supabase/migrations` (or equivalent location).

## Proposed Changes

### Database Migrations
#### [NEW] `source/database/optimize_indexes.sql` (or similar path)
Create a new SQL file to add indexes for the following tables/columns:

*   **public.employees**: `department_id`, `position_id`, `lead_id`, `auth_user_id`
*   **public.attendance_records**: `employee_id`, `created_by`
*   **public.budget_allocations**: `budget_id`, `category_id`
*   **public.budgets**: `created_by`
*   **public.employee_dependents**: `employee_id`
*   **public.expense_requests**: `employee_id`, `approved_by`, `rejected_by`
*   **public.financial_targets**: `assigned_to_id`, `created_by`
*   **public.financial_transactions**: `category_id`, `created_by`, `approved_by`, `rejected_by`
*   **public.journal_entries**: `transaction_id`, `account_id`
*   **public.leave_balances**: `employee_id`
*   **public.leave_requests**: `employee_id`

## Verification Plan

### Manual Verification
1.  **Check generated SQL**: Verify that the generated SQL contains valid `CREATE INDEX IF NOT EXISTS` statements.
2.  **Run Migration (if environment available)**: If you have a local Supabase running, we can apply the migration and check `pg_stat_user_indexes` or essentially just check the schema again. Since I don't see a running Supabase in the context, I will provide the SQL file for you to apply.
