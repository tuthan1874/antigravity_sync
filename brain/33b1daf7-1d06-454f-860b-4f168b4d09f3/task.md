# App Chấm công — Task Checklist

## Phase 1a — Foundation
- [x] DB migration (5 bảng: att_shifts, att_employee_shifts, att_records, att_requests, att_qr_sessions)
- [x] TypeScript interfaces in `types.ts`
- [x] Service layer `attendanceService.ts`
- [x] State hook `useAttendanceState.ts`
- [x] App shell `AttendanceApp.tsx` + registration in `apps.ts` & `App.tsx`
- [x] `ShiftManager.tsx` — CRUD ca làm việc + phân ca
- [x] `Dashboard.tsx` — Tổng quan + manual check-in/out

## Phase 1b — Core Features
- [x] `AttendanceLog.tsx` — Xem log chấm công
- [x] `RequestManager.tsx` — Đơn từ + duyệt
- [ ] `QrGenerator.tsx` + `QrCheckIn.tsx` — Chấm công QR (future)

## Phase 1c — Reports
- [x] `AttendanceReport.tsx` — Báo cáo tổng hợp

## Verification
- [x] TypeScript build check (0 errors)
- [x] Browser verification (all 5 tabs working)
