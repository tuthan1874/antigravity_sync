# Walkthrough — Session 2026-03-18

## 1. Expense Dashboard + Upload Biên Lai ✅

### Changes
- **[NEW]** [ExpenseDashboard.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseDashboard.tsx) — Dashboard with KPI cards, monthly bar chart, category breakdown, top 5 expenses, receipt coverage
- **[MODIFY]** [ExpenseApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseApp.tsx) — Added Dashboard tab to navigation
- **[MODIFY]** [useExpenseState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/hooks/useExpenseState.ts) — Dashboard as default tab
- **Upload biên lai** — Already working (R2 edge function v16 active)

---

## 2. Thống nhất khách hàng Invoice ↔ CRM ✅

### DB Migration
- Migrated data from `invoice_clients` → `crm_clients` (matched by name, no duplicates)
- **Dropped** `invoice_clients` table

### Code Change
- **[MODIFY]** [supabaseService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/services/supabaseService.ts) — 3 functions now use `crm_clients`:

render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/services/supabaseService.ts)

### Verification

| Test | Result |
|------|--------|
| `tsc --noEmit` | ✅ 0 errors |
| `vite build` | ✅ 148 modules, 1.74s |
| DB: `crm_clients` data intact | ✅ 3 records (Dace Marsh, KABAM, TD CONSULTING) |
| DB: `invoice_clients` dropped | ✅ |
