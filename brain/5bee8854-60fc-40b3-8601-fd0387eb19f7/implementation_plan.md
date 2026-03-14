# TD GAMES BILLING — Multi-Module Platform (Invoice + Expense)

Restructure the existing Invoice app into a multi-module **TD GAMES BILLING** platform. Add a new **Expense** module for cost tracking alongside the existing **Invoice** module for revenue tracking.

## User Review Required

> [!IMPORTANT]
> **Data Layer: Supabase (NOT NocoDB)**
> Both modules use the same Supabase project **Workflow** (`fifuhkupaqcfjwyouwpa`). Invoice tables already use `invoice_*` prefix. Expense tables will use `expense_*` prefix.

> [!IMPORTANT]
> **Client Data Sharing Strategy**
> Current client data lives in `invoice_clients`. Two options:
> - **Option A**: Expense module also reads/writes to `invoice_clients` directly
> - **Option B**: Rename `invoice_clients` → `billing_clients` (shared table) via migration
>
> **Recommend Option A** for simplicity — no migration needed, both modules reference the same table.

> [!WARNING]
> **Scope**: Dashboard module (Revenue vs Expense overview) will be a separate 3rd module later. This plan only covers Invoice + Expense.

---

## Proposed Changes

### Phase 1: App Shell — Module Navigation

#### [MODIFY] [Navbar.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/Navbar.tsx)
- Add **module switcher** (styled dropdown or segmented control) near the logo
- Options: `📄 Invoice` | `💰 Expense`
- Each module shows its own tab bar:
  - Invoice tabs: `edit`, `preview`, `history`, `dashboard`, `activity`, `recurring`
  - Expense tabs: `expenses`, `add`, `categories`, `recurring`

#### [MODIFY] [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)
- Add `activeModule` state: `'invoice' | 'expense'`
- Conditionally render Invoice or Expense module
- All existing Invoice logic stays **completely untouched**

#### [MODIFY] [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts)
- Add types: `ExpenseRecord`, `ExpenseCategory`, `RecurringExpense`

---

### Phase 2: Supabase Schema (expense_* tables)

Using the same Supabase project `fifuhkupaqcfjwyouwpa`. All tables below will be created via migration.

**`expense_categories`**
| Column | Type | Notes |
|--------|------|-------|
| id | uuid (PK) | Auto-generated |
| name | text | e.g. "Freelancer", "Server Hosting" |
| color | text | Hex color for UI |
| icon | text | Emoji or icon name |
| created_at | timestamptz | Default now() |

Default categories: Freelancer, Tool/License, Server Hosting, Tax, Salary, Equipment, Office Rent

**`expense_expenses`**
| Column | Type | Notes |
|--------|------|-------|
| id | uuid (PK) | Auto-generated |
| title | text | Expense description |
| amount | numeric | Expense amount |
| currency | text | USD or VND |
| expense_date | date | When the expense occurred |
| category_id | uuid (FK) | → expense_categories.id |
| project | text | Project name |
| client_name | text | Client name (shared data) |
| vendor | text | Who was paid |
| payment_method | text | Cash, Bank Transfer, Card |
| status | text | pending, approved, paid |
| notes | text | Additional notes |
| receipt_url | text | Receipt image URL |
| is_recurring | boolean | Flag for recurring |
| recurring_frequency | text | monthly, quarterly, yearly |
| created_by | text | Username |
| created_at | timestamptz | Auto timestamp |

**`expense_recurring`**
| Column | Type | Notes |
|--------|------|-------|
| id | uuid (PK) | Auto-generated |
| title | text | Template name |
| amount | numeric | Amount |
| currency | text | USD/VND |
| category_id | uuid (FK) | → expense_categories.id |
| project | text | Project name |
| vendor | text | Who is paid |
| frequency | text | monthly, quarterly, yearly |
| next_run | date | Next auto-generation date |
| is_active | boolean | Active flag |
| created_at | timestamptz | Auto |

---

### Phase 3: Expense Module — Components

#### [NEW] `components/expense/ExpenseApp.tsx`
Main container — manages internal tab routing (list, add/edit, categories, recurring)

#### [NEW] `components/expense/ExpenseList.tsx`
Table view with filters (category, project, client, date range, status). Monthly totals summary.

#### [NEW] `components/expense/ExpenseForm.tsx`
Add/Edit form: title, amount, currency, date, category, project, client, vendor, payment method, notes, receipt upload, recurring toggle

#### [NEW] `components/expense/ExpenseCategoryManager.tsx`
CRUD for categories with color/icon assignment

#### [NEW] `components/expense/ExpenseRecurring.tsx`
Manage recurring expense templates, show next due dates

---

### Phase 4: Expense Data Layer

#### [NEW] `services/expenseService.ts`
Supabase CRUD for `expense_expenses`, `expense_categories`, `expense_recurring`

#### [NEW] `hooks/useExpenseState.ts`
State management hook (same pattern as `useInvoiceState.ts`)

---

## Verification Plan

1. `npm run dev` → Navigate to `http://localhost:3000`
2. Verify module switcher in Navbar (Invoice ↔ Expense)
3. Switch to Expense → UI loads correctly
4. Switch back to Invoice → all Invoice features work unchanged
5. Add expense → saves to Supabase
6. Manage categories → CRUD works
7. Client dropdown shows data from shared `invoice_clients` table
