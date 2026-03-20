# Fix Invite Flow + Profile Tab

## Background

User reported 2 issues after real-world testing:
1. **Invite email goes to spam** — Supabase default template is minimal ("You have been invited"), triggers spam filters
2. **Accept Invite → skip SetPasswordScreen + no Hồ sơ tab** — Clicking invite link goes directly to dashboard, no password setup step, and Portal shows only 4 tabs (missing Hồ sơ)

## Root Cause Analysis

### Issue 1: SetPasswordScreen never shown
The Supabase JS client uses **PKCE flow** by default (not implicit flow). When user clicks the invite link:
- Supabase redirects to `https://app.tdgamestudio.com?code=<auth_code>`  
- The `supabase-js` client auto-exchanges the code for a session via `detectSessionInUrl: true` (default)
- `onAuthStateChange` fires with event = `SIGNED_IN` (NOT `PASSWORD_RECOVERY`)

Current code at `App.tsx:72-80`:
```ts
if (event === 'PASSWORD_RECOVERY' || event === 'SIGNED_IN') {
  const hash = window.location.hash;
  if (hash.includes('type=invite') || hash.includes('type=recovery') || event === 'PASSWORD_RECOVERY') {
    setNeedsPasswordSet(true);
  }
}
```

**Problem**: With PKCE flow, there's no `#type=invite` in the hash. The code was written for implicit flow where tokens come in the URL hash as `#access_token=...&type=invite`. With PKCE, it's `?code=...` and the hash is empty → `setNeedsPasswordSet(true)` never triggers.

**Fix**: Check the user's `invited_at` property and whether they've ever set a password. If `invited_at` exists and `email_confirmed_at` was just set (or user has never logged in before), show SetPasswordScreen.

### Issue 2: Missing Hồ sơ tab
The Navbar component renders all 5 tabs correctly in code. The `accessibleTabs` type is cast with `as any`. Looking at the user's screenshot more carefully, the tabs ARE: THÔNG TIN CÔNG TY, BẢNG LƯƠNG, CHẤM CÔNG, NGHỈ PHÉP — that's only 4 tabs.

The `edit` tab label is `'Hồ sơ'` and the 5th element in the `accessibleTabs` array. Since the user just accepted an invite and the app didn't go through SetPasswordScreen, the issue is likely that the user's `role` wasn't correctly set to `member` and the app didn't auto-navigate to Portal. Instead, the user manually found their way to Portal but the `currentUser.employee_id` might be missing, causing the tab to be hidden.

**Actually**, looking again at the PortalApp code, `accessibleTabs` at line 50 is a hardcoded array with all 5 tabs — there's no conditional logic. The tabs should always show. The issue might be that the 5th tab is cut off by the Navbar's CSS (overflow hidden). Let me check — the Navbar uses `flex gap-1 p-1 rounded-full` with no overflow handling, so on narrower screens 5 tabs might overflow.

**Fix**: Add `overflow-x-auto` to prevent tabs from being cut off, OR the user's screen is wide enough — let me just add the Hồ sơ tab as the first/default tab for easy visibility AND ensure the flex container scrolls.

### Issue 3: Spam email
The default Supabase invite template just says "You have been invited to create a user on https://app.tdgamestudio.com. Follow this link to accept the invite: Accept the invite". This is very generic and triggers spam filters.

**Fix**: Customize the invite email template in Supabase Dashboard to use TD Games branding.

## Proposed Changes

### App Auth Flow
#### [MODIFY] [App.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/App.tsx)
- Fix invite detection: Instead of checking URL hash for `type=invite`, check the user's metadata:
  - When `onAuthStateChange` fires with `SIGNED_IN`, check if user has `invited_at` set and `encrypted_password` is empty (first login after invite)
  - Alternative approach: Check `user.user_metadata.needs_password_set` flag (less reliable)
  - **Best approach**: Use `getSession()` on mount to check URL query param `?code=` exists AND user's `invited_at` is set. After code exchange, the session AMR (auth method reference) will contain `invite` method → use this to detect invited users

#### [MODIFY] [supabaseClient.ts](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/services/supabaseClient.ts)  
- No changes needed — `detectSessionInUrl: true` is default and handles code exchange

---

### Portal Navbar Fix
#### [MODIFY] [Navbar.tsx](file:///e:/TDC_App/TDGAMES_App/td-games-invoice-app/apps/invoice/components/Navbar.tsx)
- Add `overflow-x-auto` to tab container div to prevent tabs from being cut off
- Expand the `accessibleTabs` type union to include `'tasks'` for Portal use

---

### Email Template
- Customize Supabase Auth email templates via the Dashboard or Admin API to add TD Games branding

## Verification Plan

### Browser Test
1. Create a test employee via Quick Add  
2. Check Supabase auth log to confirm invite email sent  
3. Accept invite link → verify SetPasswordScreen is shown  
4. After setting password → verify auto-redirect to Portal  
5. Verify all 5 tabs visible including Hồ sơ  
6. Clean up test data

### Manual Verification (by anh Toàn)
- Check if invite email is now in inbox instead of spam (after template update)
