# CRM Activity Timeline

## Summary

Thêm lịch sử tương tác cho mỗi khách hàng (gọi điện, email, meeting, ghi chú). Hiển thị timeline trong trang chi tiết khách hàng + tab "Hoạt động" tổng quan toàn bộ activities.

## Proposed Changes

### Database

#### Supabase Migration: `create_crm_activities`

```sql
CREATE TABLE crm_activities (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  client_id uuid NOT NULL REFERENCES crm_clients(id) ON DELETE CASCADE,
  activity_type text NOT NULL, -- 'call' | 'email' | 'meeting' | 'note' | 'status_change'
  title text NOT NULL,
  description text DEFAULT '',
  outcome text DEFAULT '',  -- 'positive' | 'neutral' | 'negative' | ''
  activity_date timestamptz DEFAULT now(),
  actor text DEFAULT '',
  created_at timestamptz DEFAULT now()
);
CREATE INDEX idx_crm_activities_client ON crm_activities(client_id);
CREATE INDEX idx_crm_activities_date ON crm_activities(activity_date DESC);
```

---

### Types

#### [MODIFY] [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts)

Add `CrmActivity` interface after `CrmProjectFile`.

---

### Service Layer

#### [MODIFY] [crmService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/services/crmService.ts)

Add CRUD functions: `fetchActivities(clientId?)`, `createActivity()`, `deleteActivity()`.

---

### Components

#### [NEW] `ActivityTimeline.tsx`

Timeline component showing per-client activities with:
- Add activity form (type selector, title, description, outcome)
- Chronological list with activity-type icons (📞 call, 📧 email, 🤝 meeting, 📝 note)
- Delete capability
- Used inside ClientForm when editing a client

#### [MODIFY] [CrmApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/crm/components/CrmApp.tsx)

- Replace "Thống kê" tab with "Hoạt động" tab showing all recent activities across all clients

---

### Navigation Update

| Navbar slot | Before | After |
|---|---|---|
| `board` | Thống kê | Hoạt động |

## Verification

1. `tsc --noEmit` + `vite build` pass
2. Manual: open CRM → edit client → see timeline, add activity → verify it appears
