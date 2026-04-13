# GOG (Google CLI) Setup — Megahost_02 VPS

## Overview

GOG (`gog`) là Google CLI tool được cài trên VPS Megahost_02 (`180.93.144.98`) để Bot Serena (OpenClaw) có thể tương tác với Google Workspace (Gmail, Calendar, Drive, Docs, Sheets) cho account `tdconsultingvn@gmail.com`.

- **GOG version**: 0.9.0
- **Binary path**: `/usr/local/bin/gog`
- **Config directory**: `/root/.config/gogcli/`
- **GitHub**: https://github.com/steipete/gogcli

---

## Accounts

### ✅ Active: tdconsultingvn@gmail.com
- **Services**: gmail, calendar, docs, drive, sheets
- **OAuth Client**: `default`
- **Keyring password**: `SerenaGogKey2026`
- **Setup date**: 2026-04-13

### ⚠️ Legacy (broken): tdgames.vn@gmail.com
- Token encrypted với password khác (unknown), hiện lỗi `aes.KeyUnwrap(): integrity check failed`
- Cần re-auth nếu muốn dùng lại

---

## OAuth Client Details

| Field | Value |
|---|---|
| Name | Serena GOG CLI |
| Google Cloud Project | `open-493116` (OpenClaw) |
| Client ID | `826412273202-mf1gjubk3bn2js7frg27l9gnv2a2o2p9.apps.googleusercontent.com` |
| Client Secret | `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` |
| Type | Desktop app (installed) |
| Publishing status | **In production** (external) |

### Credentials file: `/root/.gog_serena/client_secret.json`
```json
{
  "installed": {
    "client_id": "826412273202-mf1gjubk3bn2js7frg27l9gnv2a2o2p9.apps.googleusercontent.com",
    "project_id": "open-493116",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "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",
    "redirect_uris": ["http://localhost"]
  }
}
```

---

## File Locations on VPS

| Path | Description |
|---|---|
| `/usr/local/bin/gog` | GOG binary |
| `/root/.config/gogcli/` | Main config directory |
| `/root/.config/gogcli/credentials.json` | OAuth credentials (loaded from client_secret.json) |
| `/root/.config/gogcli/keyring/` | Encrypted tokens |
| `/root/.gog_serena/client_secret.json` | Original OAuth client JSON |

### Keyring files:
```
/root/.config/gogcli/keyring/
├── token:default:tdconsultingvn@gmail.com
├── token:default:tdgames.vn@gmail.com
├── token:tdconsultingvn@gmail.com
└── token:tdgames.vn@gmail.com
```

---

## Usage

### ⚠️ CRITICAL: Always set GOG_KEYRING_PASSWORD

On headless VPS (no TTY), `gog` cannot prompt for keyring password. **MUST** set env var:

```bash
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com <command>
```

### Common Commands

```bash
# Gmail
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com gmail labels list
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com gmail search "is:unread"
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com gmail send --to user@example.com --subject "Test" --body "Hello"

# Calendar
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com calendar list
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com calendar events list

# Drive
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com drive list

# Docs
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com docs get <docId>

# Sheets
GOG_KEYRING_PASSWORD=SerenaGogKey2026 gog --account tdconsultingvn@gmail.com sheets get <spreadsheetId>

# Help
gog --help
gog gmail --help
```

### Shortcut with alias (optional)

Add to `/root/.bashrc`:
```bash
export GOG_KEYRING_PASSWORD=SerenaGogKey2026
alias gogtd='gog --account tdconsultingvn@gmail.com'
```

---

## Re-authentication Process

If token expires or needs refresh:

1. Load credentials:
   ```bash
   gog auth credentials /root/.gog_serena/client_secret.json
   ```

2. Start auth (with keyring password):
   ```bash
   GOG_KEYRING_PASSWORD=SerenaGogKey2026 setsid gog auth add tdconsultingvn@gmail.com --services gmail,calendar,drive,docs,sheets > /tmp/gog_auth_output.txt 2>&1 &
   sleep 5
   cat /tmp/gog_auth_output.txt
   ```

3. Copy the OAuth URL from output, open in browser

4. After Google approval, it redirects to `http://127.0.0.1:<PORT>/oauth2/callback?...`
   - If SSH tunnel is set up: callback reaches gog automatically
   - If not: copy the full callback URL and curl it from VPS:
     ```bash
     curl -s "http://127.0.0.1:<PORT>/oauth2/callback?state=...&code=...&scope=..." 
     ```

5. Verify:
   ```bash
   cat /tmp/gog_auth_output.txt
   # Should show: "Authorization received. Finishing…" and account details
   ```

### Important Notes for Re-auth:
- Port is **random** each time `gog auth add` runs
- On headless VPS, use `setsid ... &` to run in background
- Always set `GOG_KEYRING_PASSWORD` when running `gog auth add`, otherwise token won't save
- OAuth client JSON must have `installed` wrapper (not just client_id/client_secret)
- Google Cloud project must have app published to "In production" or have test users added

---

## Troubleshooting

### Error: "no TTY available for keyring file backend password prompt"
**Fix**: Set `GOG_KEYRING_PASSWORD=SerenaGogKey2026` before command

### Error: "aes.KeyUnwrap(): integrity check failed"
**Cause**: Token was encrypted with different password
**Fix**: Re-authenticate with correct `GOG_KEYRING_PASSWORD`

### Error: "invalid credentials.json"
**Cause**: JSON file missing `installed` wrapper
**Fix**: Ensure file has `{"installed": {"client_id": ..., "client_secret": ..., ...}}`

### Error: "The OAuth client was deleted" (Error 401)
**Cause**: OAuth client deleted from Google Cloud Console
**Fix**: Create new OAuth client and re-authenticate

### Error: "has not completed the Google verification process" (Error 403)
**Cause**: App in Testing mode, email not in test users list
**Fix**: Either add email to test users or publish app to production

### Error: Google 500 during OAuth
**Cause**: Temporary Google server error, often after publishing app
**Fix**: Wait 1-2 minutes and retry
