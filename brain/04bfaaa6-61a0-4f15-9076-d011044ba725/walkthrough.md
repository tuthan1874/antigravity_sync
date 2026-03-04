# SePay eInvoice Integration — Walkthrough

## What was done

### 1. Supabase Edge Function `sepay-proxy`
Deployed to project **Workflow** (`fifuhkupaqcfjwyouwpa`).
- Single function handles 2 actions: `create-draft` and `check-status`
- Token caching (23h), CORS headers, simple API key auth
- SePay credentials will be stored in Supabase Secrets (not exposed to client)

### 2. Files Changed

| File | Change |
|------|--------|
| [sePayService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/services/sePayService.ts) | 🆕 Client service: data mapping + Edge Function calls |
| [types.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/types.ts) | Added 5 eInvoice fields to `InvoiceData` |
| [nocodbService.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/services/nocodbService.ts) | Persist/parse eInvoice fields |
| [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx) | UI: button, modal, badges, payment method |
| [.env.local](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/.env.local) | Replaced 6 SEPAY credential vars with Edge Function URL |
| [constants.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/constants.ts) | Fixed pre-existing missing import |

### 3. NocoDB Schema
Added 5 columns to `INV_Invoices`: `einvoice_status`, `einvoice_reference_code`, `einvoice_tracking_code`, `einvoice_pdf_url`, `payment_method`

## Verification

- ✅ TypeScript build: **0 errors**
- ✅ App loads correctly at `http://localhost:3000/`
- ✅ New "Xuất HĐ Điện Tử" button visible in Actions sidebar
- ✅ Payment method pills visible in Discount & Tax section

![App with eInvoice UI](file:///C:/Users/dangt/.gemini/antigravity/brain/04bfaaa6-61a0-4f15-9076-d011044ba725/einvoice_and_payment_method_verification_1772643637608.png)

## ⚠️ Remaining: Set Supabase Secrets

The Edge Function needs SePay credentials stored as **Supabase Secrets**. Go to:

**[Supabase Dashboard → Workflow → Settings → Edge Functions](https://supabase.com/dashboard/project/fifuhkupaqcfjwyouwpa/settings/functions)**

Add these secrets:
```
SEPAY_BASE_URL=https://einvoice-api.sepay.vn
SEPAY_CLIENT_ID=EINV-LIVE-30FNB2UCPW315TF2
SEPAY_CLIENT_SECRET=7603cde31d4208308f737bac243eef49
SEPAY_PROVIDER_ACCOUNT_ID=d83e6718-0a8b-11f1-b21a-a6006ab65aca
SEPAY_TEMPLATE_CODE=1
SEPAY_INVOICE_SERIES=C26TSE
SEPAY_PROXY_API_KEY=tdgames-sepay-2026
```

After setting secrets, the eInvoice button will be fully functional — no code changes needed.
