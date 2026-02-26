# Migrate Google Drive Sync to OAuth 2.0

We will migrate the Google Drive integration from using a Service Account to standard OAuth 2.0 User Auth so that the user can use their standard Google Account (`tdgames.vn@gmail.com`) to sync files without having to manually share folders.

## User Setup Required

> [!IMPORTANT]
> You will need to create an OAuth 2.0 Client ID in the Google Cloud Console and add the following to your `.env` file:
> ```
> GOOGLE_CLIENT_ID=your_client_id
> GOOGLE_CLIENT_SECRET=your_client_secret
> GOOGLE_REDIRECT_URI=http://localhost:3000/api/auth/google/callback
> ```

## Proposed Changes

### Configuration
#### [MODIFY] `src/config.js`
- Remove `GOOGLE_SERVICE_ACCOUNT_KEY_PATH`
- Add `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GOOGLE_REDIRECT_URI`

### Backend Changes
#### [NEW] `src/drive/auth.js`
- Create an OAuth2 client instance using `googleapis`.
- Implement a method to generate the Google Auth URL.
- Implement a method to handle the callback, exchange the authorization code for tokens, and listen for token refresh events.

#### [MODIFY] `src/drive/sync.js`
- Modify `initDriveService` to remove the Service Account setup.
- Instead, retrieve the `GOOGLE_DRIVE_TOKENS` from the NocoDB `Settings` table.
- Initialize the Google Drive API client (`google.drive`) using the OAuth2 client and the stored tokens.

#### [MODIFY] `src/api.js`
- Add an endpoint `GET /api/auth/google/url` to return the Google Auth URL.
- Add an endpoint `GET /api/auth/google/callback` to handle the OAuth redirect, retrieve the tokens, and save them to the NocoDB `Settings` table via `nocodb.upsertSetting('GOOGLE_DRIVE_TOKENS', JSON.stringify(tokens))`.
- Add an endpoint `GET /api/auth/google/status` to check if tokens exist in the database.

## Verification Plan

### Automated Tests
- Run `npm run dev` and ensure no startup errors occur.

### Manual Verification
1. User navigates to `http://localhost:3000/api/auth/google/url`.
2. User copies the provided URL into their browser, logs in with `tdgames.vn@gmail.com`, and grants access.
3. The browser redirects to `http://localhost:3000/api/auth/google/callback` and says "Authentication successful!".
4. Wait 5 minutes (or run a manual sync script) to verify that Drive folders sync successfully using the newly acquired tokens.
