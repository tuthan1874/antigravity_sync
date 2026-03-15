# Workforce Task Sync Enhancement

## Tasks
- [x] Plan changes: add start_date, closed_date, payment tracking to wf_tasks
- [x] Database migration: add `start_date`, `closed_date`, `payment_status` columns to `wf_tasks`
- [x] Update TypeScript types (`WorkforceTask` in `types.ts`)
- [x] Update `TaskList.tsx` sync logic to populate `start_date` and `closed_date` (with `date_updated` fallback)
- [x] Update `TaskList.tsx` UI to show start/closed dates + payment status
- [x] Update `SettlementManager.tsx` to filter by closed_date and accumulate unpaid tasks
- [x] Update `workforceService.ts` `createSettlement` to mark tasks as `paid`
- [x] Verify in browser — dates and payment badges showing correctly
