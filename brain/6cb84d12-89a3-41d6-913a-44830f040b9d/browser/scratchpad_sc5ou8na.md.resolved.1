# Task: Debug Freelancer Invite Flow

## Checklist
- [x] Open http://localhost:3000/#hr
- [x] Find and click "Thêm nhanh" button
- [x] Toggle to "Freelancer" mode
- [x] Fill in:
    - Họ tên: Test Debug FL
    - Email cá nhân: testdebugfl@gmail.com
    - Specialization: VFX
    - Level: Junior
- [x] Click "Thêm & Gửi invite"
- [x] Wait for 5 seconds
- [x] Capture browser console logs and screenshot
- [x] Analyze the logs for "[Auth]", "error", "Failed", or network errors related to "create-employee-auth"

## Findings
- The "Quick Add" modal switched to Freelancer mode successfully.
- Freelancer "Test Debug FL" (FL-006) was created and appears in the HR list.
- Browser console log: `[Auth] Freelancer invite sent to testdebugfl@gmail.com`.
- The `hrService.ts` received a successful response from the Supabase Edge Function `create-employee-auth`.
- Since the edge function returned 200 OK, the issue is likely external to the frontend/edge function code:
    - Supabase SMTP rate limits (3 emails/hour on free tier).
    - SMTP not configured in Supabase Dashboard.
    - Email arrived in Spam folder.
- Observation: "Gửi lại Invite" button is missing for Freelancers in the UI, unlike Fulltime employees. This might be a separate UI bug or intentional, but it confirms that the "invite" state might not be fully reflected for freelancers in the current UI.
