# CRM App — Task List

## Database
- [x] Create `crm_clients` table in Supabase
- [x] Migrate data from `invoice_clients` + `fb_clients`
- [x] Enable RLS policies

## Frontend
- [x] Add `CrmClient` type to `types.ts`
- [x] Create `apps/crm/services/crmService.ts`
- [x] Create `apps/crm/hooks/useCrmState.ts`
- [x] Create `apps/crm/components/ClientList.tsx`
- [x] Create `apps/crm/components/ClientForm.tsx`
- [x] Create `apps/crm/components/CrmApp.tsx`

## Integration
- [x] Register CRM in `config/apps.ts`
- [x] Add CRM route in `App.tsx`

## Verification
- [x] TypeScript compile check — clean, no errors
- [x] Browser test — 3 clients loaded, CRUD functional
