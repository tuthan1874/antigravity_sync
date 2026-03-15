# CRM App — Walkthrough

## What was built
App CRM quản lý khách hàng tập trung — app thứ 4 trên TD Games Platform.

## Database
- Bảng `crm_clients`: 17 columns (name, type, contact, email, phone, address, country, tax_code, website, industry, status, tags, notes...)
- RLS enabled with open policy
- Migrated 3 records từ `invoice_clients` (2) + `fb_clients` (1, deduped)

## Frontend Files
| File | Purpose |
|------|---------|
| `apps/crm/services/crmService.ts` | Supabase CRUD |
| `apps/crm/hooks/useCrmState.ts` | State + filtering + search |
| `apps/crm/components/ClientList.tsx` | List + stats cards + search/filter |
| `apps/crm/components/ClientForm.tsx` | Add/edit form with tags |
| `apps/crm/components/CrmApp.tsx` | App shell with navbar |

## Integration
- `config/apps.ts`: CRM entry (👥, blue gradient)
- `App.tsx`: CRM route `#crm`
- `types.ts`: `CrmClient` interface

## Verification

````carousel
![Home screen — CRM as 4th app](file:///C:/Users/dangt/.gemini/antigravity/brain/c8091b7d-5055-460e-a9fd-6d2849cebec3/home_screen_with_crm_1773585255929.png)
<!-- slide -->
![CRM client list with 3 migrated records](file:///C:/Users/dangt/.gemini/antigravity/brain/c8091b7d-5055-460e-a9fd-6d2849cebec3/crm_client_list_1773585273516.png)
````

- ✅ TypeScript compile clean
- ✅ 3 clients loaded from migration
- ✅ Navbar with exchange rate + "Khách hàng" / "Thống kê" tabs
- ✅ Stats cards, search, filter, inline CRUD
