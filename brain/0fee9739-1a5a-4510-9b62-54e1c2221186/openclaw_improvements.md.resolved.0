# 🔧 Gợi ý cải thiện OpenClaw Setup

## 🔴 Ưu tiên CAO (Nên làm ngay)

### 1. Tạo systemd service cho OpenClaw Gateway
Hiện tại OpenClaw gateway chạy trực tiếp, không có PM2 hay systemd. **Nếu VPS restart, OpenClaw sẽ chết.**

```bash
# Tạo /etc/systemd/system/openclaw.service
[Unit]
Description=OpenClaw AI Gateway
After=network-online.target cliproxy.service
Wants=network-online.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/openclaw
ExecStart=/usr/bin/openclaw gateway --bind loopback --port 18789
Restart=always
RestartSec=5
Environment=HOME=/root
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```
```bash
systemctl daemon-reload
systemctl enable openclaw
systemctl start openclaw
```

### 2. Cập nhật OpenClaw lên phiên bản mới nhất
Đang chạy **v2026.4.3**, mới nhất là **v2026.4.11** (chênh 8 phiên bản!)

```bash
cd /root/openclaw
git pull origin main
pnpm install
pnpm build  # nếu cần
systemctl restart openclaw  # sau khi tạo service
```

### 3. Bảo mật CLIProxyAPI
Port 8317 đang mở public ra internet → bất kỳ ai biết API key đều dùng được models miễn phí.

**Giải pháp:**
```yaml
# /root/CLIProxyAPI/config.yaml
host: "127.0.0.1"  # Chỉ cho localhost truy cập
remote-management:
  allow-remote: false  # Tắt quản lý từ xa
```
Hoặc dùng firewall:
```bash
ufw deny 8317
# Hoặc chỉ cho localhost:
iptables -A INPUT -p tcp --dport 8317 ! -s 127.0.0.1 -j DROP
```

### 4. Đổi API key CLIProxyAPI
Key hiện tại `toandung@040723` quá yếu và dễ đoán.
```bash
# Tạo key mạnh:
openssl rand -hex 32
# Cập nhật trong /root/CLIProxyAPI/config.yaml
# Cập nhật trong /root/.openclaw/agents/*/agent/models.json
```

---

## 🟡 Ưu tiên TRUNG BÌNH

### 5. Tạo file `.env` cho OpenClaw
Hiện tại không có `.env` → tất cả secrets nằm trực tiếp trong `openclaw.json`. Nên tách ra:

```bash
# /root/.openclaw/.env
OPENCLAW_GATEWAY_TOKEN=649a8029f9d553a1f8e39eb8c8380acf9bc4283e9e610ea1

# Telegram
TELEGRAM_BOT_TOKEN_DEFAULT=7501103702:AAHKBvaemaZnwbjKXJqcohY8un92pvQ7sh4
TELEGRAM_BOT_TOKEN_CTO=8211147557:AAFsp06duVNjyeeO4VAjymc9DQiiQMIP3P8
TELEGRAM_BOT_TOKEN_PM=8704802697:AAEisNATCOn27SEHICC9ZYAkIOh__M_4RN0
TELEGRAM_BOT_TOKEN_SERENA=8306342659:AAGkx0c5lkWchT6TyHYg1LG6Pr4JvI8fEYE

# Discord
DISCORD_BOT_TOKEN_DEFAULT=MTQyNjA5OTQ1Nzg3MDUyODYzOA...
DISCORD_BOT_TOKEN_CTO=MTQ3OTUxMTU0NTc5NjEwNDQyMg...
DISCORD_BOT_TOKEN_PM=MTQ3OTUyOTk3MDk0MTU1ODc5Ng...

# Tools
BRAVE_API_KEY=BSAZeMUYRJfnG8xY7bXMnXBNC6RerMp
```

### 6. Bật lại Cron Jobs (nếu cần)
Cả 2 cron jobs (Gmail check 9h/17h + Urgent monitor 30 phút) đều đang **disabled**.

Nếu muốn bật lại:
```bash
openclaw cron enable db3372de-f861-49b5-9110-534088c3b76d  # Daily check
openclaw cron enable 92ce0f6a-844f-4056-9dd9-16bfad0b0799  # Urgent monitor
```

### 7. Thêm Discord binding cho Serena
Serena hiện chỉ hoạt động trên Telegram. Nếu cần trên Discord:
```json
// Thêm vào bindings array trong openclaw.json
{
  "agentId": "serena_nguyen",
  "match": {
    "channel": "discord",
    "accountId": "serena_nguyen"
  }
}
```
Và tạo Discord bot + account config tương ứng.

### 8. Fix Discord default account
Discord `default` account không có guild nào trong config riêng → có thể không phục vụ server nào. Cần thêm guilds:
```json
"default": {
  "token": "...",
  "groupPolicy": "allowlist",
  "streaming": "off",
  "guilds": {
    "YOUR_GUILD_ID": {
      "requireMention": true
    }
  }
}
```

### 9. Xóa file rác trong repo
```bash
rm "/root/openclaw/ion hiện tại so với remote"
```

### 10. Dùng SSH key thay vì password
File `.env` trên máy local chứa password VPS dạng plaintext. Nên chuyển sang SSH key:
```bash
# Trên máy local:
ssh-keygen -t ed25519
ssh-copy-id root@180.93.144.98
```

---

## 🟢 Ưu tiên THẤP (Nice to have)

### 11. Agent auth profiles đều rỗng
Tất cả `auth.json` cho agents đều là `{}`. Điều này có nghĩa agents không có per-agent auth riêng → dùng chung auth từ `models.json`. Không phải lỗi nhưng nếu cần phân quyền model khác nhau cho từng agent thì cần cấu hình.

### 12. Tăng `maxTokens` cho models
Hiện tại tất cả models giới hạn `maxTokens: 8192`. Với các model mạnh như Claude Opus/GPT-5.2 có thể tăng lên 16384 hoặc cao hơn.

### 13. Monitoring & Alerting
- Thêm health check endpoint monitoring (UptimeKuma/BetterStack)
- Cảnh báo khi gateway down
- Giám sát disk usage (đang 66%, còn 28GB)

### 14. Backup config định kỳ
```bash
# Thêm vào crontab:
0 2 * * * tar -czf /root/backups/openclaw-$(date +\%Y\%m\%d).tar.gz /root/.openclaw/openclaw.json /root/.openclaw/workspace/ /root/.openclaw/cron/
```

### 15. Compaction mode
Đang dùng `"compaction": {"mode": "safeguard"}` → OK, giữ nguyên để tránh mất context quan trọng.

---

## Tổng kết

| Hạng mục | Số lượng |
|---|---|
| 🔴 Ưu tiên Cao | 4 items |
| 🟡 Ưu tiên Trung bình | 6 items |
| 🟢 Ưu tiên Thấp | 5 items |

**Top 3 việc cần làm ngay:**
1. ⚡ Tạo systemd service cho OpenClaw (tránh mất khi reboot)
2. 🔒 Khóa port 8317 CLIProxyAPI (bảo mật nghiêm trọng)
3. 📦 Cập nhật OpenClaw v2026.4.3 → v2026.4.11
