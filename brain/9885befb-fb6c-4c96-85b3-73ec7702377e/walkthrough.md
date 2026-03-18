# Walkthrough — Session 2026-03-18

## 1. Expense Dashboard + Upload Biên Lai ✅

- **[NEW]** [ExpenseDashboard.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseDashboard.tsx) — KPI cards, monthly bar chart, category breakdown, top 5 expenses
- **[MODIFY]** [ExpenseApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/components/ExpenseApp.tsx) + [useExpenseState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/expense/hooks/useExpenseState.ts) — Dashboard tab as default

---

## 2. Thống nhất khách hàng Invoice ↔ CRM ✅

- **DB**: Migrated `invoice_clients` → `crm_clients`, dropped old table
- **[MODIFY]** [supabaseService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/services/supabaseService.ts) — 3 client functions now use `crm_clients`

---

## 3. Supabase Auth Migration ✅

### DB: Auth Users Created

| Email | Password | Role |
|-------|----------|------|
| `admin@tdgames.local` | `TDGames@2026` | admin |
| `member@tdgames.local` | `Member@2026` | member |

> [!IMPORTANT]
> Login dùng username (admin/member), hệ thống tự map sang `username@tdgames.local`.

### Frontend Changes

#### [MODIFY] [supabaseService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/services/supabaseService.ts)

- `loginWithCredentials` → `supabase.auth.signInWithPassword()`
- Added `logoutFromAuth()` and `getAuthUser()`

render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/services/supabaseService.ts)

#### [MODIFY] [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)

- Session restore via `supabase.auth.getSession()`
- Live auth state via `onAuthStateChange()`
- Logout via `supabase.auth.signOut()`
- Added auth loading spinner
- Removed all `localStorage.invoice_user` logic

render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)

#### [MODIFY] [useInvoiceState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/hooks/useInvoiceState.ts)

- Removed duplicate localStorage auth logic
- Auth now managed solely by `App.tsx`

render_diffs(file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/hooks/useInvoiceState.ts)

### Fallback

`invoice_accounts` table + RPC `invoice_verify_login` preserved — can revert if needed.

### Verification

| Test | Result |
|------|--------|
| `tsc --noEmit` | ✅ 0 errors |
| `vite build` | ✅ 1.75s |
| Browser test | ⏳ Manual — see below |

### Manual Test

1. Mở [http://localhost:3001/](http://localhost:3001/)
2. Login: username `admin`, password `TDGames@2026`
3. Verify home screen loads
4. Refresh page (F5) — verify **vẫn logged in** (session persists)
5. Logout → verify quay về login screen
