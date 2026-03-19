# Workforce Settlement: Thuế TNCN 10% + Bonus trên tổng hoá đơn

## Mô tả
Thêm 2 tính năng cho Nghiệm thu (Settlement) trong Workforce app:
1. **Auto trừ 10% thuế TNCN** trên tổng giá trị nghiệm thu
2. **Bonus trên tổng hoá đơn** — nhập thủ công, hỗ trợ 2 kiểu: theo % hoặc số tiền cụ thể

### Công thức tính:
```
Tổng giá tasks          = SUM(task.price)
Bonus trên tổng         = (theo % hoặc số tiền cụ thể — nhập thủ công)
Tổng trước thuế         = Tổng giá tasks + Bonus
Thuế TNCN (10%)         = Tổng trước thuế × 10%
THỰC NHẬN              = Tổng trước thuế − Thuế TNCN
```

---

## Proposed Changes

### Database (Supabase Migration)

#### [MODIFY] `wf_settlements` table
Thêm 4 cột mới:
- `bonus_type` — `text`, default `'amount'` (giá trị: `'percent'` hoặc `'amount'`)
- `bonus_value` — `numeric`, default `0` (giá trị % hoặc số tiền)
- `bonus_amount` — `numeric`, default `0` (số tiền bonus đã tính)
- `tax_rate` — `numeric`, default `10` (mặc định 10% TNCN)
- `tax_amount` — `numeric`, default `0` (số tiền thuế đã tính)
- `net_amount` — `numeric`, default `0` (thực nhận sau thuế)

---

### TypeScript Types

#### [MODIFY] [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts)
Thêm các fields mới vào `Settlement` interface:
- `bonus_type`, `bonus_value`, `bonus_amount`
- `tax_rate`, `tax_amount`, `net_amount`

---

### Service Layer

#### [MODIFY] [workforceService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/services/workforceService.ts)
- Update `createSettlement()` — thêm params `bonus_type`, `bonus_value`, `tax_rate`; tính `bonus_amount`, `tax_amount`, `net_amount` rồi lưu DB
- Update `updateSettlement()` — support update bonus/tax fields

---

### UI Components

#### [MODIFY] [SettlementManager.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/components/SettlementManager.tsx)

**Create View** — Thêm phần nhập Bonus + hiển thị:
- Dropdown chọn `bonus_type`: "Theo %" hoặc "Số tiền"
- Input nhập `bonus_value`
- Hiển thị preview bảng tính: Tổng tasks → +Bonus → -TNCN 10% → Thực nhận

**Detail View** — Cập nhật phần summary:
- Thêm card: Bonus, Thuế TNCN, Thực nhận
- Cập nhật bảng tổng footer với dòng Bonus, Thuế, Thực nhận

**List View** — Hiển thị `net_amount` (thực nhận) thay vì `total_amount` trên card

**PDF Export** — Thêm dòng Bonus, Thuế TNCN, Thực nhận vào section totals

---

## Verification Plan

### Browser Testing
1. Mở `http://localhost:3000/`, login admin
2. Vào Workforce → Nghiệm thu → Tạo nghiệm thu mới
3. Chọn nhân sự, chọn tasks, nhập Bonus (thử cả % và số tiền)
4. Verify preview tính đúng: Tổng + Bonus - 10% TNCN = Thực nhận
5. Tạo nghiệm thu, vào Detail, verify các card summary hiển thị đúng
6. Export PDF, verify có dòng Bonus + TNCN + Thực nhận
