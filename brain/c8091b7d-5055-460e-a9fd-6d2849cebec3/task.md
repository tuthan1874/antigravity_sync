# Redesign Nghiệm Thu (Settlement)

- [x] Backend: Fix `createSettlement` — không auto-mark paid
- [x] Backend: Fix `deleteSettlement` — rollback tasks to unpaid
- [x] Backend: Fix `updateSettlement` — mark paid khi status=paid
- [x] UI: Rewrite `SettlementManager.tsx` — List View + Detail View + Create Form
- [x] UI: Add PDF export (window.print)
- [x] Wiring: Pass `vcbSellRate` + refresh tasks on delete
- [x] Verify in browser
