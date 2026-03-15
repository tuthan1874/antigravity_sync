# Browser Testing: CRM Document List Drag-Drop and Preview

## Checklist
- [x] Navigate to http://localhost:3000/#crm
- [x] Verify "TÀI LIỆU" tab content
- [x] Verify "Xem" and "Tải" buttons on existing documents
- [x] Verify "＋ Thêm tài liệu" form with drag-drop area
- [x] Test preview modal functionality

## Findings
- Successfully navigated to the CRM Document tab.
- "👁️ Xem" and "⬇️ Tải" buttons are visible on the existing document "STATEMENT OF WORK NO. 1 ...".
- The "+ Thêm tài liệu" form features a new drag-drop upload area: "📤 Kéo thả file vào đây hoặc click để chọn (tối đa 20MB)".
- The preview modal opens correctly when clicking "👁️ Xem", showing the filename and action buttons (Mở tab mới, Download, Đóng).
- Note: The iframe preview showed an auth error for the specific file, but the modal UI and buttons are functional.
- Icons and file size (e.g., "518.1 KB") are displayed correctly in the list.
