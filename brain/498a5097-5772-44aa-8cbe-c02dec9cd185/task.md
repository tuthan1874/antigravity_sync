# Monthly Invoice Feature

## Done
- [x] Backend: GET `/api/pm-tracking/invoice` route (filter closed + unpaid tasks, group by assignee)
- [x] Backend: POST `/api/pm-tracking/invoice/mark-paid` route (batch update)
- [x] Backend: Fix logic — only include tasks with Closed_Date
- [x] Frontend: Separate Invoice tab in sidebar (🧾 Monthly Invoice)
- [x] Frontend: Page section with header, month picker, assignee dropdown
- [x] Frontend: html2canvas CDN for PNG export
- [x] Frontend: `generateInvoice()` with premium UI (summary bar, gradient header, OVERDUE badges)
- [x] Frontend: `exportInvoicePNG()` and `markInvoicePaid()`

## TODO (Next Session)
- [ ] Verify invoice generation works with redesigned UI in browser
- [ ] Test Export PNG functionality
- [ ] Test Mark All Paid batch update
- [ ] Review UI on light/dark themes
- [ ] Handle edge cases (no data, mixed currencies)
