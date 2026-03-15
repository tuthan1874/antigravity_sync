# Task: Debug file URL for CRM documents

## Plan
1. [x] Navigate to http://localhost:3000/#crm
2. [x] Click "TÀI LIỆU" tab
3. [x] Identify the file URL for an existing document
4. [x] Verify if it's using the S3 API endpoint or the Public URL
5. [x] Report findings

## Findings
- Found file URL: `https://642ba1c41caae845c62667d7810b4eb9.r2.cloudflarestorage.com/expense-receipts/1773587439852_oao2vm.pdf`
- The URL is using the R2 S3-style API endpoint (`r2.cloudflarestorage.com`), which requires authentication and is not suitable for public iframe embedding or direct public access.
- This confirms that the Edge Function is returning the internal/authenticated URL instead of the public access URL.
