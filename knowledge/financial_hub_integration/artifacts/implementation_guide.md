# Financial Hub Integration Guide

## Overview
3-phase integration connecting all financial modules (Invoice, Payroll, Workforce) into a unified Expense module via Postgres triggers.

**Supabase Project:** `fifuhkupaqcfjwyouwpa`
**Commit:** `f57f4b5` on `main`

---

## Phase 1: Auto-Sync Triggers

### Schema Changes (expense_expenses)
| Column | Type | Purpose |
|--------|------|---------|
| `type` | text ('expense'/'revenue') | Distinguish costs from income |
| `source_type` | text | Origin: payroll, settlement, invoice, manual |
| `source_id` | uuid | FK to source record |

### DB Triggers
| Trigger | Source Table | Fires On | Creates |
|---------|------------|----------|---------|
| `trg_settlement_to_expense` | `wf_settlements` | status → 'paid' | expense (Freelancer cost) |
| `trg_payroll_to_expense` | `pay_payroll_sheets` | status → 'confirmed' | expense (Payroll cost) |
| `trg_invoice_to_expense` | `invoice_invoices` | status → 'paid' | revenue (Project income) |

### Auto Categories
- 💼 Lương nhân viên (#3B82F6)
- 🎨 Freelancer (#8B5CF6)
- 💰 Doanh thu dự án (#10B981)

### Important: Invoice items use `unitPrice` NOT `amount`
```sql
COALESCE((item->>'unitPrice')::numeric, COALESCE((item->>'amount')::numeric, 0))
* COALESCE((item->>'quantity')::numeric, 1)
```

---

## Phase 2: Financial Hub Dashboard

### Components Modified
- **ExpenseDashboard.tsx** — Revenue vs Expense P&L chart, monthly P&L table, source breakdown, USD revenue by client
- **ExpenseList.tsx** — Type tabs (All/Expense/Revenue), source filter, P&L summary cards, auto-synced protection
- **useExpenseState.ts** — Added `filterType`, `filterSource`, separate `revenueVND/USD`, `expenseVND/USD` totals
- **types.ts** — Added `type`, `source_type`, `source_id` to `ExpenseRecord`

---

## Phase 3: Budget, Forecast & Export

### Database
```sql
CREATE TABLE expense_budgets (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  month int, year int,
  category_id uuid REFERENCES expense_categories(id),
  label text, amount numeric, currency text,
  UNIQUE(month, year, category_id, currency)
);
```

### Components
- **ExpenseReports.tsx** — Budget tracker, 3-month forecast, CSV export
- **ExpenseApp.tsx** — Added 'reports' tab to navigation (`#expense/reports`)

### Export Function
`exportToCSV(expenses, filename)` — Generates UTF-8 BOM CSV with columns: Date, Type, Source, Title, Amount, Currency, Category, Vendor, Status, Notes.
