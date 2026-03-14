# TD GAMES Platform — App Launcher

## Phase 1: Restructure Folders (Option A)
- [ ] Create `apps/invoice/components/`, `apps/invoice/hooks/`, `apps/invoice/services/`
- [ ] Move Invoice components → `apps/invoice/components/`
- [ ] Move `useInvoiceState.ts` → `apps/invoice/hooks/`
- [ ] Move Invoice services → `apps/invoice/services/`
- [ ] Keep `supabaseClient.ts` in root `services/` (shared)
- [ ] Keep `LoginScreen.tsx`, `FormElements.tsx`, `Button.tsx`, `ToastNotification.tsx` in root `components/` (shared)
- [ ] Update ALL import paths in moved files
- [ ] Build test — 0 errors

## Phase 2: Home Screen + App Router
- [ ] Create `config/apps.ts` (app registry)
- [ ] Create `components/HomeScreen.tsx` (app launcher grid)
- [ ] Modify `App.tsx` for activeApp routing
- [ ] Modify Invoice Navbar for ← Back button
- [ ] Build + browser test

## Phase 3: Expense App
- [ ] Create Supabase tables (expense_categories, expense_expenses, expense_recurring)
- [ ] Create `apps/expense/services/expenseService.ts`
- [ ] Create `apps/expense/hooks/useExpenseState.ts`
- [ ] Create Expense components (ExpenseApp, List, Form, Categories, Recurring)
- [ ] Build + browser test

## Phase 4: Final Verification
- [ ] Full flow test: Login → Home → Invoice → Back → Expense → Back
- [ ] Commit + Push to GitHub
