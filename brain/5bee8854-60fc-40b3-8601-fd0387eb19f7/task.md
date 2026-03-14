# Workforce App — Phase 1

## Database
- [x] Create `wf_workers` table
- [x] Create `wf_contracts` table
- [x] Create `wf_tasks` table
- [x] Create `wf_settlements` + `wf_settlement_tasks` tables
- [x] Enable RLS on all tables

## Frontend — Types & Services
- [x] Add Workforce types to `types.ts`
- [x] Create `workforceService.ts` (Supabase CRUD)

## Frontend — Components
- [x] Create `WorkforceApp.tsx` (shell + shared Navbar)
- [x] Create `WorkerList.tsx` (danh sách nhân sự)
- [x] Create `WorkerForm.tsx` (thêm/sửa nhân sự + hợp đồng)
- [x] Create `TaskList.tsx` (danh sách task)
- [x] Create `SettlementManager.tsx` (nghiệm thu tháng)

## App Registration
- [x] Add to `config/apps.ts`
- [x] Add route in `App.tsx`

## Hooks
- [x] Create `useWorkforceState.ts`

## Verification
- [x] TypeScript build passes (0 errors)
- [x] Browser test: full flow verified
