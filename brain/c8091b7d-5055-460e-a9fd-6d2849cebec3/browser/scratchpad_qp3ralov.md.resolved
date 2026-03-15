# Task: Test R2 Expense Upload via Edge Function

## Plan
- [x] Go to http://localhost:3000/#expense/add
- [x] Execute test upload script via JavaScript
- [x] Wait 8 seconds for response
- [x] Check console logs for success/failure
- [x] Capture screenshot
- [x] Report results

## Findings
- URL: http://localhost:3000/#expense/add
- Edge Function: https://fifuhkupaqcfjwyouwpa.supabase.co/functions/v1/r2-expense-upload
- Script result: `ERROR:TypeError: Failed to fetch` (in title and console)
- CORS Issue: `Access-Control-Allow-Origin` header missing on the response.
- Server Error (logged in console as 'Test Result'): `Upload failed: 400 ... <Code>InvalidBucketName</Code><Message>The specified bucket name is not valid.</Message>`
- Screenshot captured: `expense_add_form_initial_...`
