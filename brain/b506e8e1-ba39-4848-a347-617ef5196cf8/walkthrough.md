# TD Games Billing App — Session Walkthrough

## Completed Work (2026-03-12/13)

### Migration: NocoDB → Supabase
- All tables created with `invoice_` prefix on Supabase project `workflow` (`fifuhkupaqcfjwyouwpa`)
- Tables: `invoice_studios`, `invoice_banks`, `invoice_clients`, `invoice_invoices`, `invoice_accounts`
- All data migrated (2 studios, 2 banks, 2 clients, 5 invoices, 2 accounts)
- RLS enabled on all tables
- Created [supabaseClient.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/services/supabaseClient.ts) and [supabaseService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/services/supabaseService.ts)

### P1 Optimizations ✅
| # | Item | Status |
|---|---|---|
| 1 | Delete `nocodbService.ts` + migration script | ✅ Done |
| 2 | Hash passwords (bcrypt) + RPC `invoice_verify_login` | ✅ Done |
| 3 | Replace N8N → SePay Edge Function for PDF download | ✅ Done |

### P2 UX Improvements ✅
| # | Item | Status |
|---|---|---|
| 4 | `useInvoiceState()` hook — App.tsx: 521→105 lines | ✅ Done |
| 5 | Clone/Duplicate invoice button on History cards | ✅ Done |
| 6 | Multi-currency dashboard (USD/VND separated) | ✅ Done |
| 7 | PDF export via Edge Function | ⏭️ Skipped (window.print() sufficient) |

### Git
- Commit: `d4435a1` on `main` branch
- Repo: `tdgamesvn/tdgames_billing`
- 37 files changed, +9,712 / −2,077 lines

## Remaining P3 Items (Future)
- Supabase Realtime for live updates
- Activity log / audit trail
- Recurring invoices
- Email notifications for invoices
- Cloudflare R2 storage integration (secrets already configured in Supabase)

## Key Architecture

```
App.tsx (105 lines, render only)
  └─ useInvoiceState() hook (hooks/useInvoiceState.ts)
      ├─ supabaseService.ts (CRUD for all tables)
      ├─ supabaseClient.ts (Supabase init)
      └─ sePayService.ts (eInvoice creation + PDF download)

Components:
  Navbar, InvoiceEditor, HistoryTab, DashboardTab,
  EInvoiceModals, FilterBar, ToastNotification, LoginScreen
```

## Environment
- `.env.local`: Supabase URL + Anon Key + SePay config (gitignored)
- Dev server: `npm run dev` on port 3001
- Supabase project: `fifuhkupaqcfjwyouwpa` (workflow)

## Screenshots

````carousel
![Multi-currency Dashboard](file:///C:/Users/dangt/.gemini/antigravity/brain/b506e8e1-ba39-4848-a347-617ef5196cf8/dashboard_multicurrency_verified_1773338049103.png)
<!-- slide -->
![Clone Invoice Result](file:///C:/Users/dangt/.gemini/antigravity/brain/b506e8e1-ba39-4848-a347-617ef5196cf8/cloned_invoice_editor_1773337366100.png)
````
