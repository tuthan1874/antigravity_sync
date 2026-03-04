# Task: Test SePay eInvoice API CORS

## Plan
- [x] Open a browser page at `https://www.google.com`
- [x] Execute fetch request with SePay credentials
- [x] Monitor result in page title and console logs
- [x] Document result (Success/CORS Error)
- [x] Finalize findings

## Progress
- Tested CORS from Google origin.
- Result: **CORS FAILED**.
- Error: `Access to fetch at 'https://einvoice-api.sepay.vn/v1/token' from origin 'https://www.google.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.`
- Decision: Must use a proxy (Supabase Edge Function) for API calls.
