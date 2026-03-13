# P3 Features — TD Games Billing App

## Background

The billing app migration from NocoDB → Supabase is complete (P1+P2 done). P3 adds four production-grade enhancements: Realtime sync, Activity log, Recurring invoices, and Email notifications.

**Supabase project**: `fifuhkupaqcfjwyouwpa` (workflow)

---

## P3-1: Supabase Realtime for Live Updates

Subscribe to Postgres changes on invoice tables so multi-user sessions auto-sync without manual refresh.

### Supabase Config
- Enable Realtime on `invoice_invoices` table via Supabase publication setting (no DDL needed, just alter publication)

### [MODIFY] [supabaseClient.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/services/supabaseClient.ts)
- Already initialised, no changes needed

### [MODIFY] [useInvoiceState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/hooks/useInvoiceState.ts)
- Add `useEffect` that subscribes to `supabase.channel('invoice-changes')` listening for INSERT/UPDATE/DELETE on `invoice_invoices`
- On event → call `loadHistory()` + show toast (`notify(...)`)
- Clean up channel on unmount / logout
- Simple, no new files needed

---

## P3-2: Activity Log / Audit Trail

### Database Migration

#### [NEW] Table `invoice_activity_logs`
| Column | Type | Notes |
|--------|------|-------|
| `id` | uuid PK | `gen_random_uuid()` |
| `invoice_id` | uuid FK → `invoice_invoices.id` | ON DELETE CASCADE |
| `action` | text | `created`, `updated`, `status_changed`, `deleted`, `einvoice_created` etc. |
| `actor` | text | username or 'system' |
| `details` | jsonb | old/new values |
| `created_at` | timestamptz | `now()` |

- Enable RLS (allow all authenticated)
- Create DB trigger function `log_invoice_change()` that fires AFTER INSERT/UPDATE/DELETE on `invoice_invoices` and auto-inserts a row into `invoice_activity_logs`

### Service Layer

#### [MODIFY] [supabaseService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/services/supabaseService.ts)
- Add `fetchActivityLogs(invoiceId?: string, limit?: number)` — fetches from `invoice_activity_logs` ordered by `created_at DESC`
- Add `logActivity(invoiceId, action, actor, details)` — for manual logging from frontend (e.g., eInvoice creation, PDF export)

### UI

#### [NEW] [ActivityLogTab.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/ActivityLogTab.tsx)
- Timeline-style display of activity log entries
- Filter by invoice number, action type, date range
- Matches existing dark/light theme system
- Auto-refresh via Realtime subscription (piggyback on P3-1)

#### [MODIFY] [Navbar.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/Navbar.tsx)
- Add `'activity'` tab (admin only, with 📋 icon)

#### [MODIFY] [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)
- Import and render `ActivityLogTab` when `activeTab === 'activity'`

#### [MODIFY] [useInvoiceState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/hooks/useInvoiceState.ts)
- Expand `activeTab` type to include `'activity'`
- Add `accessibleTabs` entry for admin
- Add `activityLogs` state + `loadActivityLogs()` function

---

## P3-3: Recurring Invoices

### Database Migration

#### [NEW] Table `invoice_recurring`
| Column | Type | Notes |
|--------|------|-------|
| `id` | uuid PK | `gen_random_uuid()` |
| `name` | text | Template name |
| `frequency` | text | `monthly`, `quarterly`, `yearly` |
| `next_run` | date | Next auto-generation date |
| `client_info` | jsonb | Same structure as `invoice_invoices` |
| `studio_info` | jsonb | |
| `banking_info` | jsonb | |
| `items` | jsonb | Template line items |
| `currency` | text | Default `'USD'` |
| `tax_rate` | numeric | Default `0` |
| `is_active` | boolean | Default `true` |
| `last_generated_at` | timestamptz | |
| `created_at` | timestamptz | |

### Service Layer

#### [MODIFY] [supabaseService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/services/supabaseService.ts)
- Add CRUD functions: `fetchRecurringTemplates()`, `saveRecurringTemplate()`, `updateRecurringTemplate()`, `deleteRecurringTemplate()`, `toggleRecurringActive()`

### UI

#### [NEW] [RecurringTab.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/RecurringTab.tsx)
- List all recurring templates with status badges (Active/Paused)
- Create/Edit modal with same client/studio/items structure as InvoiceEditor
- Frequency selector + next run date
- Toggle active/pause
- Delete with confirmation

#### [MODIFY] Navbar, App.tsx, useInvoiceState.ts
- Add `'recurring'` tab (admin only, with 🔄 icon)

### Edge Function

#### [NEW] `process-recurring-invoices`
- Supabase Edge Function triggered by pg_cron (daily at 00:00 UTC)
- Queries `invoice_recurring` where `is_active = true AND next_run <= today`
- Creates new invoice in `invoice_invoices` from template
- Updates `next_run` based on frequency
- Logs activity to `invoice_activity_logs`

---

## P3-4: Email Notifications

### Edge Function

#### [NEW] `send-invoice-email`
- Accepts: `to`, `subject`, `invoiceNumber`, `htmlBody`, `attachmentUrl?`
- Uses Resend API (free tier, 100 emails/day)
- Returns success/error

### Database Migration
- Add columns to `invoice_invoices`: `email_sent_at` (timestamptz nullable), `email_sent_to` (text nullable)

### UI

#### [NEW] [EmailModal.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/EmailModal.tsx)
- Recipient input (pre-filled from client email)
- Subject line (pre-filled: "Invoice {number} from {studio}")
- Body preview (HTML email template)
- Send button with loading state

#### [MODIFY] HistoryTab.tsx
- Add ✉️ email button on each invoice card

#### [MODIFY] useInvoiceState.ts
- Add `handleSendEmail(invoiceId)` handler
- Email modal state management

---

## Verification Plan

### Automated Checks
1. **TypeScript compilation**: `npx tsc --noEmit` in `e:\TDC_App\TDGAMES_App\td-games-invoice-app`
2. **Vite build**: `npm run build` — ensures no bundling errors

### Browser Tests (via browser_subagent)
1. **P3-1 Realtime**: Open app → Navigate to History → Modify a record via Supabase SQL → Verify toast appears and list updates
2. **P3-2 Activity**: Login as admin → Click Activity tab → Verify log entries appear for past actions
3. **P3-3 Recurring**: Login as admin → Click Recurring tab → Create a template → Verify it appears in list
4. **P3-4 Email**: Login as admin → Go to History → Click email icon → Verify modal opens with pre-filled data

### Manual Verification (by user)
1. Open two browser tabs with the app → Edit invoice in one → Confirm other tab updates automatically (P3-1)
2. Check Supabase dashboard for `invoice_activity_logs` entries after performing CRUD operations (P3-2)
