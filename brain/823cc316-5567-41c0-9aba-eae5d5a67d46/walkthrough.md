# Walkthrough — Workforce Settlement: Thuế TNCN + Bonus

## Tính năng đã triển khai

### 1. Auto trừ 10% Thuế TNCN
Tất cả nghiệm thu (settlement) tự động tính thuế TNCN 10% trên tổng trước thuế.

### 2. Bonus trên tổng hoá đơn
Cho phép nhập thêm Bonus khi tạo nghiệm thu:
- **Theo %** — tính % trên tổng giá tasks
- **Số tiền cụ thể** — nhập trực tiếp số tiền

### Công thức
```
Tổng tasks → +Bonus → Tổng trước thuế → −10% TNCN → Thực nhận
```

## Files đã thay đổi

| File | Thay đổi |
|------|----------|
| **DB** `wf_settlements` | +6 cột: `bonus_type`, `bonus_value`, `bonus_amount`, `tax_rate`, `tax_amount`, `net_amount` |
| [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts) | `Settlement` interface: thêm bonus/tax/net fields |
| [workforceService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/services/workforceService.ts) | `computeSettlementTotals()` helper + extended `createSettlement()` |
| [useWorkforceState.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/hooks/useWorkforceState.ts) | `handleCreateSettlement()` truyền bonus/tax params |
| [SettlementManager.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/workforce/components/SettlementManager.tsx) | Create/Detail/List/PDF — full UI update |

## Screenshots

![Settlement List](C:/Users/dangt/.gemini/antigravity/brain/823cc316-5567-41c0-9aba-eae5d5a67d46/settlements_list_page_1773920266754.png)

![Create Form with Bonus & Tax](C:/Users/dangt/.gemini/antigravity/brain/823cc316-5567-41c0-9aba-eae5d5a67d46/create_settlement_form_bonus_tax_1773920280926.png)

## Verification
- ✅ `tsc --noEmit` — No errors
- ✅ Browser UI — Form hiển thị đúng: Loại Bonus, Bonus value, Thuế TNCN 10%
- ✅ Preview tính toán live khi chọn tasks
