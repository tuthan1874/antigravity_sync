# Login Screen & Role-Based Access Control

Add a simple internal login screen backed by NocoDB `INV_Accounts` table. Role `admin` sees all tabs; role `member` sees only `edit` and `preview`.

## Proposed Changes

### 1. NocoDB — INV_Accounts table
**[DONE via MCP]** Table `INV_Accounts` created with columns:
- `username` (SingleLineText, unique, required)
- `password` (SingleLineText, required)
- `role` (SingleSelect: `admin` | `member`)

#### [MODIFY] .env.local
Add `VITE_NOCODB_ACCOUNTS_TABLE_ID=<id returned from create_table>`

---

### 2. Auth Service

#### [MODIFY] services/nocodbService.ts
Add `loginWithCredentials(username, password)` function that:
- Calls NocoDB GET on `INV_Accounts` with `where=(username,eq,X)~and(password,eq,Y)`
- Returns `{ id, username, role }` or throws error if not found

---

### 3. Types

#### [MODIFY] types.ts
Add:
```ts
export interface AccountUser {
  id: string;
  username: string;
  role: 'admin' | 'member';
}
```

---

### 4. Login Screen Component

#### [NEW] components/LoginScreen.tsx
A beautiful full-screen login card with:
- TD Games Billing branding (logo + title)
- Username & password inputs
- Login button with loading state
- Error message on failed login
- Dark-themed, glassmorphism style matching the app aesthetic

---

### 5. App.tsx — Auth Gate & Role-Based Tabs

#### [MODIFY] App.tsx
- Add state: `currentUser: AccountUser | null` (default `null`)
- If `currentUser === null` → render `<LoginScreen onLogin={setCurrentUser} />`
- If logged in → render app as normal, but:
  - Tab list: `admin` → `['edit', 'preview', 'history', 'dashboard']`; `member` → `['edit', 'preview']`
  - Add logout button in navbar (top-right)
  - Show username in navbar

---

## Verification Plan

### Manual Verification
1. Open http://localhost:3000 → login screen appears
2. Enter wrong credentials → error message shown
3. Login as `admin` → all 4 tabs visible
4. Logout and login as `member` → only `edit` and `preview` tabs visible
5. Admin can access `history` and `dashboard`; member cannot navigate to those tabs
