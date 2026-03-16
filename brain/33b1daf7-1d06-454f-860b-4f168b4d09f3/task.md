# App Chấm công — Task Checklist

## Phase 1a — Foundation
- [/] DB migration (5 bảng: att_shifts, att_employee_shifts, att_records, att_requests, att_qr_sessions)
- [ ] TypeScript interfaces in `types.ts`
- [ ] Service layer `attendanceService.ts`
- [ ] State hook `useAttendanceState.ts`
- [ ] App shell `AttendanceApp.tsx` + registration in `apps.ts` & `App.tsx`
- [ ] `ShiftManager.tsx` — CRUD ca làm việc
- [ ] `Dashboard.tsx` — Tổng quan + manual check-in/out

## Phase 1b — Core Features
- [ ] `AttendanceLog.tsx` — Xem log chấm công
- [ ] `ShiftAssignment.tsx` — Phân ca cho nhân viên
- [ ] `RequestManager.tsx` — Đơn từ + duyệt
- [ ] `QrGenerator.tsx` + `QrCheckIn.tsx` — Chấm công QR

## Phase 1c — Reports
- [ ] `AttendanceReport.tsx` — Báo cáo tổng hợp

## Verification
- [ ] TypeScript build check
- [ ] Browser verification
