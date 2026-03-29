# Nghiệm Thu Theo Dự Án — Walkthrough

## Tính năng

Cho phép nghiệm thu task hoàn thành **theo dự án (ClickUp folder)** thay vì chỉ theo Freelancer, để gửi cho **khách hàng**.

## Thay đổi

| File | Mô tả |
|---|---|
| [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts#L213-L231) | Thêm `ProjectAcceptance`, `ProjectAcceptanceTask` interfaces |
| [projectAcceptanceService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/services/projectAcceptanceService.ts) | **[NEW]** CRUD: fetch, create, update, delete, fetchTasks |
| [ProjectAcceptanceManager.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/components/ProjectAcceptanceManager.tsx) | **[NEW]** 3 views: List, Create, Detail. PDF export cho KH |
| [useWorkforceState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/hooks/useWorkforceState.ts) | State + CRUD handlers cho project acceptances |
| [WorkforceApp.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/components/WorkforceApp.tsx) | Thêm tab "NT Dự Án" vào navbar |

**DB Migration**: `wf_project_acceptances` + `wf_project_acceptance_tasks` (Supabase, RLS enabled)

## Kết quả

````carousel
![NT Dự Án — List View](C:/Users/dangt/.gemini/antigravity/brain/abf809c3-49a7-4b2b-aa6d-c02e16d9c119/project_acceptance_page_1774756021013.png)
<!-- slide -->
![Tạo NT Dự Án — Form](C:/Users/dangt/.gemini/antigravity/brain/abf809c3-49a7-4b2b-aa6d-c02e16d9c119/create_project_acceptance_form_1774756032169.png)
````

![Browser test recording](C:/Users/dangt/.gemini/antigravity/brain/abf809c3-49a7-4b2b-aa6d-c02e16d9c119/test_project_acceptance_1774755984296.webp)

## Luồng sử dụng

1. Vào **Workforce App** → tab **"NT Dự Án"**
2. Click **"✚ Tạo NT dự án"** → Chọn KH (Space) → Chọn Dự án (Folder) → Chọn tasks approved → Submit
3. Xem detail → Chuyển trạng thái: **Draft → Đã gửi KH → KH đã duyệt**
4. Chọn đơn vị (TD Games / TD Consulting) → **Export PDF** gửi cho khách hàng
