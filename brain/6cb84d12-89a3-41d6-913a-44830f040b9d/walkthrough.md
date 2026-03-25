# Freelancer Portal — Walkthrough

## Tổng kết

Đã triển khai đầy đủ Freelancer Portal cho phép freelancer đăng nhập, hoàn thiện hồ sơ, và xem tasks/nghiệm thu/dashboard thu nhập.

## Files đã thay đổi

| File | Thay đổi |
|---|---|
| [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts) | Thêm role `freelancer` + `worker_id` vào `AccountUser` |
| [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx) | Freelancer routing, profile completion role-aware, `worker_id` extraction |
| [apps.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/config/apps.ts) | Thêm Freelancer Portal app config |
| [ProfileCompletionScreen.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/components/ProfileCompletionScreen.tsx) | Freelancer-specific fields (bỏ avatar, thêm MST bắt buộc) |
| [hrService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/hr/services/hrService.ts) | Auto-invite freelancer qua email cá nhân |
| [FreelancerPortalApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/freelancer-portal/components/FreelancerPortalApp.tsx) | **NEW** — Portal 4 tabs: Dashboard, Tasks, Settlements, Profile |
| [freelancerPortalService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/freelancer-portal/services/freelancerPortalService.ts) | **NEW** — Service queries cho freelancer portal |
| [create-employee-auth/index.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/supabase/functions/create-employee-auth/index.ts) | **NEW** — Updated edge function hỗ trợ role + worker_id |

## Chi tiết triển khai

### 1. Auth & Routing
- Role `freelancer` thêm vào `AccountUser` và `VALID_ROLES`
- Login → detect role → redirect đến `#freelancer-portal`
- Profile completion dùng required fields khác cho freelancer

### 2. Freelancer Portal App (4 Tabs)
- **📊 Dashboard** — KPI cards (tổng task, hoàn thành, thu nhập đã nhận, chờ TT) + bar chart 6 tháng
- **📋 Tasks** — Danh sách task với filter (Tất cả / Đang làm / Hoàn thành / Đã duyệt)
- **📑 Nghiệm thu** — Grid phiếu nghiệm thu, click xem chi tiết (bao gồm bảng task, tổng/thuế/thực nhận)
- **👤 Hồ sơ** — Reuse `ProfileTab` từ Employee Portal

### 3. Invite Flow
- HR tạo freelancer → auto gửi invite qua email cá nhân (field `email`)
- Edge function nhận thêm `role: 'freelancer'` + `worker_id` → set vào user_metadata
- Freelancer mở link → SetPassword → ProfileCompletion (CTV) → FreelancerPortal

### 4. Profile Completion (CTV)
- Title: "Hoàn Thiện Hồ Sơ CTV" (amber theme)
- Bỏ: avatar bắt buộc, temp_address, insurance_number
- Thêm: MST (Mã số thuế) **bắt buộc**

## Build Status
- ✅ Vite production build passes
- ✅ App loads correctly, auth guards work

## Cần làm tiếp (Manual Steps)

> [!IMPORTANT]
> **2 bước cần deploy thủ công:**

1. **DB Migration** — Chạy SQL:
```sql
ALTER TABLE hr_employees ADD COLUMN IF NOT EXISTS worker_id UUID REFERENCES wf_workers(id);
```

2. **Edge Function** — Deploy updated `create-employee-auth` từ `supabase/functions/create-employee-auth/index.ts` lên Supabase
