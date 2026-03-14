# Workforce App — Phase 1

## Database
- [ ] Create `wf_workers` table
- [ ] Create `wf_contracts` table
- [ ] Create `wf_tasks` table
- [ ] Create `wf_settlements` + `wf_settlement_tasks` tables
- [ ] Enable RLS on all tables

## Frontend — Types & Services
- [ ] Add Workforce types to `types.ts`
- [ ] Create `workforceService.ts` (Supabase CRUD)

## Frontend — Components
- [ ] Create `WorkforceApp.tsx` (shell + shared Navbar)
- [ ] Create `WorkerList.tsx` (danh sách nhân sự)
- [ ] Create `WorkerForm.tsx` (thêm/sửa nhân sự + hợp đồng)
- [ ] Create `TaskList.tsx` (danh sách task)
- [ ] Create `SettlementManager.tsx` (nghiệm thu tháng)

## App Registration
- [ ] Add to `config/apps.ts`
- [ ] Add route in `App.tsx`

## Hooks
- [ ] Create `useWorkforceState.ts`

## Verification
- [ ] TypeScript build passes
- [ ] Browser test: full flow
