# Invite Flow & HR Admin Actions — Session Progress

## Completed Today (2026-03-20)

### 1. Metadata-Driven Onboarding Flow
- Rewrote `App.tsx` to detect invited users via `user_metadata.invited_at` + `password_set` flags (not URL params)
- `SetPasswordScreen` marks `password_set: true` after successful password change
- Profile completion check now queries **database on every session load** → F5 bypass fixed

### 2. Mandatory Profile Completion
- Rewrote `ProfileCompletionScreen.tsx` — no skip button
- **14 required fields** grouped into 4 sections:
  - 👤 Thông tin cá nhân (7): name, email, phone, DOB, gender, 2 addresses
  - 🪪 Thông tin CCCD (3): number, issue date, issue place  
  - 🏦 Thông tin ngân hàng (3): bank name, account, holder name
  - 📄 Thuế & Bảo hiểm (2, optional): tax code, insurance number
- Avatar required (120×120 square, changeable on hover)
- Desktop: single viewport, 2-column section layout, no scroll
- Mobile: responsive, scrollable

### 3. HR Admin Actions
- Deployed `manage-employee-auth` edge function (Supabase)
- Added `resendInvite()` + `resetEmployeePassword()` to `hrService.ts`
- Added 📧 Re-invite + 🔑 Reset Password hover buttons on `EmployeeList.tsx`

### 4. Deploy Script Fix
- Fixed `deploy.yml`: backup `.env` → `git reset --hard` → restore `.env` (no more stash conflicts)

## Key Files Modified
| File | Changes |
|------|---------|
| `App.tsx` | Metadata onboarding, DB profile check on session load |
| `ProfileCompletionScreen.tsx` | Full rewrite: grouped sections, no skip, avatar required |
| `SetPasswordScreen.tsx` | Sets `password_set: true` in metadata |
| `hrService.ts` | Added `resendInvite`, `resetEmployeePassword` |
| `EmployeeList.tsx` | Re-invite + Reset Password buttons |
| `HrApp.tsx` | Wired `onToast` to EmployeeList |
| `.github/workflows/deploy.yml` | Robust deploy with .env backup/restore |

## Pending / To Test Tomorrow
- [ ] Full end-to-end test: create employee → invite email → set password → fill profile → access app
- [ ] Test re-invite button from HR list
- [ ] Test reset password button from HR list
- [ ] Verify F5 no longer bypasses profile completion
- [ ] Check avatar upload works on profile completion screen
- [ ] Verify mobile responsive layout
- [ ] Employee deletion should clean up Supabase Auth user (not yet implemented)
