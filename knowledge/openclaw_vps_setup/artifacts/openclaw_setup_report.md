# OpenClaw VPS Setup - Báo cáo kiểm tra toàn diện
> **Ngày kiểm tra:** 2026-04-12 22:28 (GMT+7)  
> **VPS:** 180.93.144.98 (vps6core)

---

## 1. Thông tin hệ thống VPS

| Thông số | Giá trị |
|---|---|
| **OS** | Ubuntu 22.04 (5.15.0-164-generic) x86_64 |
| **CPU** | 6 cores |
| **RAM** | 9.7 GB (đang dùng 3.1 GB, còn trống 6.2 GB) |
| **Swap** | 8 GB (dùng 53 MB) |
| **Disk** | 84 GB (dùng 52 GB = 66%, còn 28 GB) |
| **Node.js** | v22.22.0 |
| **pnpm** | 10.33.0 |
| **OpenClaw binary** | `/usr/bin/openclaw` |

---

## 2. OpenClaw Installation

| Thông số | Giá trị | Trạng thái |
|---|---|---|
| **Version** | 2026.4.3 | ⚠️ Cũ (latest: v2026.4.11) |
| **Git branch** | `main` | ✅ OK |
| **Install path** | `/root/openclaw/` | ✅ OK |
| **State dir** | `/root/.openclaw/` | ✅ OK |
| **Config** | `/root/.openclaw/openclaw.json` | ✅ OK |
| **.env** | ❌ Không tồn tại `/root/openclaw/.env` NOR `/root/.openclaw/.env` | ⚠️ Thiếu |

### Git Status
- Branch: `main` (commit: `b118efea80`)
- **Outdated**: 8 tags mới hơn (v2026.4.5 → v2026.4.11)
- Modified file: `pnpm-lock.yaml`
- Junk file: `"ion hiện tại so với remote"` (file rác trong repo)

---

## 3. Gateway Status

| Thông số | Giá trị | Trạng thái |
|---|---|---|
| **Health endpoint** | `http://127.0.0.1:18789/healthz` → `{"ok":true,"status":"live"}` | ✅ Healthy |
| **Port 18789** | LISTEN (loopback only) | ✅ OK |
| **Bind mode** | `loopback` | ✅ Secure |
| **Auth mode** | Token-based | ✅ OK |
| **Gateway token** | `649a8029f9d553a1f8e39eb8c8380acf9bc4283e9e610ea1` | ✅ Set |

### Running Processes
```
openclaw-gateway  PID=3336990  CPU=21.2%  MEM=435MB  ✅ Running
openclaw          PID=3341493  CPU=0.4%   MEM=59MB   ✅ Running
openclaw          PID=3341960  CPU=132%   MEM=302MB  ✅ Running (active task)
```

### ⚠️ Vấn đề tự khởi động
- **Không có systemd service** cho OpenClaw gateway
- **PM2 trống** (không có process nào trong PM2)
- OpenClaw đang chạy trực tiếp (không qua PM2/systemd) → **Nếu VPS restart, OpenClaw sẽ không tự khởi động lại!**

---

## 4. CLIProxyAPI (Model Proxy)

| Thông số | Giá trị | Trạng thái |
|---|---|---|
| **Service** | `cliproxy.service` (systemd) | ✅ Enabled + Running |
| **Port** | 8317 (all interfaces) | ⚠️ Mở public |
| **Uptime** | 2 tháng 4 ngày | ✅ Stable |
| **API Key** | `toandung@040723` | ⚠️ Yếu |
| **Binary** | `/root/CLIProxyAPI/cli-proxy-api` | ✅ OK |
| **Remote management** | `allow-remote: true` | ⚠️ Rủi ro bảo mật |

---

## 5. Agents Configuration

### 5.1 Agent List (4 agents)

| Agent ID | Model mặc định | Identity | Emoji | Workspace | Trạng thái |
|---|---|---|---|---|---|
| `main` (Tony) | `cliproxy/gpt-5.2` | Tony Dang - AI Assistant | 😎 | `/root/.openclaw/workspace` | ✅ OK |
| `td_cto` | `cliproxy/gpt-5.2` | TD_CTO - CTO | 🧠 | `/root/.openclaw/workspace-td_cto` | ✅ OK |
| `td_pm` | `cliproxy/gpt-5.2` | TD_PM - PM | 📋 | `/root/.openclaw/workspace-td_pm` | ✅ OK |
| `serena_nguyen` | `cliproxy/gpt-5.2` | Serena Nguyen - EA | 🗂️ | `/root/.openclaw/workspace-serena_nguyen` | ✅ OK |

### 5.2 Agent Workspace Files

Tất cả 4 agents đều có đầy đủ:
- ✅ `SOUL.md` - Persona & nguyên tắc hoạt động
- ✅ `IDENTITY.md` - Thông tin định danh
- ✅ `USER.md` - Thông tin người dùng
- ✅ `MEMORY.md` - Quy tắc sử dụng memory (Mem0 + Qdrant)
- ✅ `memory/` directory
- ✅ `.openclaw/` directory
- ✅ `.pi/` directory

### 5.3 Default Model Config

```json
{
  "primary": "cliproxy/gemini-3-flash-preview",
  "imageModel": "cliproxy/gemini-3-pro-image-preview"
}
```

### 5.4 Chiến lược Model (từ MEMORY.md)
1. **Kỹ thuật:** `gemini-claude-opus-4-5-thinking` → `gpt-5.3-codex` → `gemini-3-pro-preview`
2. **Thông thường:** `gemini-3-flash-preview`
3. Tất cả đi qua CLIProxyAPI (`cliproxy:local` port 8317)

### 5.5 Available Models (qua CLIProxyAPI)

| Model ID | Name | Reasoning | Input |
|---|---|---|---|
| `gemini-3-flash-preview` | Gemini 3 Flash Preview | ❌ | text, image |
| `gemini-3-pro-preview` | Gemini 3 Pro Preview | ✅ | text, image |
| `gemini-3-pro-image-preview` | Gemini 3 Pro Image | ✅ | text, image |
| `gemini-claude-sonnet-4-5` | Claude Sonnet 4.5 | ✅ | text, image |
| `gemini-claude-sonnet-4-5-thinking` | Claude Sonnet Thinking | ✅ | text, image |
| `gemini-claude-opus-4-5-thinking` | Claude Opus Thinking | ✅ | text, image |
| `gpt-5.2` | GPT-5.2 | ✅ | text, image |
| `gpt-5.3-codex` | GPT-5.3 Codex | ✅ | text |
| `gpt-5.2-codex` | GPT-5.2 Codex | ✅ | text |
| `gpt-5` | GPT-5 | ✅ | text, image |
| `gpt-5-codex` | GPT-5 Codex | ✅ | text |

> Tất cả models đều cost = 0 (qua proxy, không tính phí trực tiếp)

---

## 6. Channel Integrations

### 6.1 Telegram (4 bots)

| Account | Bot Token (masked) | DM Policy | Allow From | Streaming | Trạng thái |
|---|---|---|---|---|---|
| `default` (→ main) | `7501103702:AAH...` | allowlist | `1131287322` | partial | ✅ |
| `td_cto` | `8211147557:AAF...` | allowlist | `1131287322` | partial | ✅ |
| `td_pm` | `8704802697:AAE...` | allowlist | `1131287322` | partial | ✅ |
| `serena_nguyen` | `8306342659:AAG...` | allowlist | `1479984548` | partial | ✅ |

### 6.2 Discord (3 accounts)

| Account | Guilds | Require Mention | Streaming | Trạng thái |
|---|---|---|---|---|
| `default` (→ main) | (none explicitly) | N/A | off | ⚠️ Không có guild |
| `td_cto` | `1268245697111785598`, `1476480923267629199` | ✅ | off | ✅ |
| `td_pm` | `1297749891468230727`, `945559215039209513` | ✅ | off | ✅ |

**Discord guilds cấp top-level:**
- `1268245697111785598` ✅
- `1297749891468230727` ✅
- `1476480923267629199` ✅

> ⚠️ Discord `default` account không có guild nào → bot default trên Discord sẽ không phục vụ guild nào

### 6.3 Serena trên Discord
- ⚠️ **Không có binding Discord** cho `serena_nguyen` — Serena chỉ hoạt động trên Telegram

---

## 7. Bindings (Agent ↔ Channel)

| Agent | Telegram | Discord |
|---|---|---|
| `main` | ✅ `default` | ✅ `default` |
| `td_cto` | ✅ `td_cto` | ✅ `td_cto` |
| `td_pm` | ✅ `td_pm` | ✅ `td_pm` |
| `serena_nguyen` | ✅ `serena_nguyen` | ❌ Không có |

---

## 8. Plugins & Tools

| Plugin | Enabled | Config |
|---|---|---|
| Telegram | ✅ | Default |
| Discord | ✅ | Default |
| Brave Search | ✅ | API Key set |
| Web Search | ✅ | Built-in |
| Web Fetch | ✅ | Built-in |
| GOG (Google) | ✅ | Account: tdgames.vn@gmail.com |

---

## 9. Cron Jobs

| Job | Schedule | Agent | Status | Trạng thái |
|---|---|---|---|---|
| Daily Gmail + Calendar check | `0 9,17 * * *` (Asia/Saigon) | main | **DISABLED** | ⚠️ Tắt |
| Urgent mail monitor | Every 30 min | main | **DISABLED** | ⚠️ Tắt |

Cả 2 cron đều đang **disabled** (`enabled: false`).

---

## 10. Other Services on VPS

| Container | Image | Port | Status |
|---|---|---|---|
| Open WebUI | `ghcr.io/open-webui/open-webui:main` | 3000→8080 | ✅ Healthy (2 months) |
| Stirling PDF | `frooodle/s-pdf:latest` | 8081→8080 | ✅ Up (6 weeks) |
| Qdrant | `qdrant/qdrant:latest` | 6333 | ✅ Up (2 months) |

---

## 11. Security Concerns

| Vấn đề | Mức độ | Chi tiết |
|---|---|---|
| CLIProxyAPI mở public port 8317 | 🔴 **Cao** | Ai cũng truy cập được từ internet |
| CLIProxyAPI remote management = true | 🔴 **Cao** | Cho phép quản lý từ xa |
| CLIProxyAPI API key yếu | 🟡 **Trung bình** | `toandung@040723` dễ đoán |
| Bot tokens trong config file | 🟡 **Trung bình** | Nên dùng env variables |
| Wordpress probe từ bên ngoài | 🟡 **Trung bình** | Logs cho thấy bot scan WP |
| VPS password trong .env trên local | 🟡 **Trung bình** | Nên dùng SSH key |

---

## 12. Credentials Summary (Masked)

| Service | Key/Token |
|---|---|
| **Gateway Token** | `649a8029...e610ea1` |
| **CLIProxyAPI Key** | `toandung@040723` |
| **Brave Search API** | `BSAZeM...erMp` |
| **GOG Client ID** | `744795499244-...` |
| **GOG Client Secret** | `GOCSPX-3GP...44Tc` |
| **Gmail Credentials** | File: `/root/.openclaw/gmail-credentials.json` |
| **Telegram Bots** | 4 bots (tokens in config) |
| **Discord Bots** | 3 bots (tokens in config) |
