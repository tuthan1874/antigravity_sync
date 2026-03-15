# Nghiệm Thu Redesign — Walkthrough

## Changes Made

### Backend (`workforceService.ts`)
- **`createSettlement`** — No longer auto-marks tasks as `paid`. Tasks stay `unpaid` until user explicitly marks the settlement as "Đã thanh toán"
- **`deleteSettlement`** — Rollbacks all linked tasks to `unpaid`, deletes link records, then deletes settlement
- **`updateSettlement`** — When status transitions to `paid`, marks all linked tasks as `payment_status: 'paid'`

### Hook (`useWorkforceState.ts`)
- Added task state refresh after `handleUpdateSettlement` (when status changes) and `handleDeleteSettlement`

### UI (`SettlementManager.tsx`) — Complete Rewrite
3 views replacing the old single-view component:

**List View** — Summary cards (Total, Paid, Unpaid, Amount) + settlement cards with click-to-detail

**Detail View** — Full task table with all columns (#, Task, Client, Project, Closed Date, Price, Currency, VNĐ Equiv, Bonus, Bonus Note, Notes). Action bar with status workflow, PDF export, delete

**Create View** — Worker/period selection, task selection with price/bonus preview, breadcrumb hierarchy, VNĐ conversion preview

### PDF Export
In-browser `window.open` + `print` with professional layout: header, metadata, full task table, totals, signature areas

## Screenshots

````carousel
![List View](C:\Users\dangt\.gemini\antigravity\brain\c8091b7d-5055-460e-a9fd-6d2849cebec3\settlement_list_view_with_card_1773554387172.png)
<!-- slide -->
![Detail View](C:\Users\dangt\.gemini\antigravity\brain\c8091b7d-5055-460e-a9fd-6d2849cebec3\settlement_detail_view_1773554401759.png)
<!-- slide -->
![PDF Export](C:\Users\dangt\.gemini\antigravity\brain\c8091b7d-5055-460e-a9fd-6d2849cebec3\settlement_pdf_preview_1773554482221.png)
````

![Demo Recording](C:\Users\dangt\.gemini\antigravity\brain\c8091b7d-5055-460e-a9fd-6d2849cebec3\settlement_redesign_test_1773554308442.webp)
