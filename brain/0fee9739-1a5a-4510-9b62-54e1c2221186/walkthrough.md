# OpenClaw VPS Audit & Improvements — Walkthrough

## Tóm tắt

Đã kiểm tra toàn diện OpenClaw trên VPS `180.93.144.98` và thực hiện 4 cải thiện ưu tiên cao.

---

## Kiểm tra đã thực hiện

| Hạng mục | Kết quả |
|---|---|
| Gateway health | ✅ `{"ok":true,"status":"live"}` |
| 4 Agents (main, td_cto, td_pm, serena) | ✅ Đầy đủ SOUL/IDENTITY/USER/MEMORY |
| Telegram (4 bots) | ✅ Configured đúng, allowlist + streaming |
| Discord (3 bots) | ✅ Hoạt động, requireMention |
| CLIProxyAPI (model proxy) | ✅ Running, 11 models available |
| Qdrant (memory) | ✅ Docker healthy, port 6333 |
| Systemd autostart | ✅ User-level systemd enabled |
| Bindings agent↔channel | ✅ Logic đúng |

---

## Cải thiện đã thực hiện

### ✅ 1. Xác nhận Systemd Service
- Gateway đã có systemd service tại `~/.config/systemd/user/openclaw-gateway.service`
- Status: `enabled + active (running)`
- Tự khởi động khi VPS reboot ✅

### ✅ 2. Bảo mật CLIProxyAPI
**Trước:**
- Port 8317 mở toàn bộ interfaces (`host: ""`) → public internet
- Remote management bật (`allow-remote: true`)

**Sau:**
```diff
- host: ""
+ host: "127.0.0.1"

-   allow-remote: true
+   allow-remote: false
```

- Service đã restart, chỉ listen `127.0.0.1:8317` ✅
- Config backup tại: `/root/CLIProxyAPI/config.yaml.bak.20260412_223449`

### ✅ 3. Cập nhật OpenClaw
**Trước:** v2026.4.3 (April 3)  
**Sau:** v2026.4.11 (latest, April 12)

Quy trình:
1. `git pull origin main` — Fast-forward (4 files changed)
2. `pnpm install` — +3 packages, -213 cleaned
3. `pnpm build` — Full rebuild (tsdown + plugin-sdk + canvas + A2UI)
4. `node patch.js` — Patch matrix-js-sdk (3 files)
5. `systemctl --user restart openclaw-gateway`
6. Health check: `{"ok":true,"status":"live"}` ✅

### ✅ 4. Cleanup
- File rác `"ion hiện tại so với remote"` đã được xóa trước đó

---

## Còn lại (cần Toàn quyết định)

| # | Việc | Cần gì |
|---|---|---|
| 5 | Đổi API key CLIProxyAPI (`toandung@040723` → key mạnh) | Confirm đổi, update tất cả agent models.json |
| 6 | Bật cron Gmail/Calendar (đang disabled) | Confirm có muốn bật? |
| 7 | Thêm guilds cho Discord default bot | Cung cấp guild IDs |
| 8 | Thêm Discord cho Serena | Cần tạo Discord bot mới |

---

## Files đã tạo/sửa

| File | Mục đích |
|---|---|
| `fix_security.sh` | Script bảo mật CLIProxyAPI |
| `update_openclaw.sh` | Script update OpenClaw |
| `run_script.py` | Helper upload+run scripts qua SSH |
| `check_gateway.sh` | Script kiểm tra gateway process |

## Knowledge Item đã lưu

Toàn bộ thông tin OpenClaw (config, agents, channels, credentials, system) đã được lưu tại:
- [openclaw_setup_report.md](file:///C:/Users/dangt/.gemini/antigravity/knowledge/openclaw_vps_setup/artifacts/openclaw_setup_report.md)

Sẽ được tự động tham khảo trong các conversation tương lai.
