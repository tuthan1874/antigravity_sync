# Sửa Lỗi Clawdbot Agent 🔧

## Vấn Đề
Lệnh `clawdbot agent --message "..."` bị lỗi:
```
Error: Pass --to <E.164>, --session-id, or --agent to choose a session
```

## Nguyên Nhân
1. Thiếu flag `--agent` 
2. API key có thể chưa được cấu hình đúng

## Giải Pháp

### 1. Sử Dụng Lệnh Đúng
```bash
# ĐÚNG - Cần thêm flag --agent
clawdbot agent --agent --message "Câu hỏi của bạn"

# VÍ DỤ:
clawdbot agent --agent --message "Tạo checklist cho dự án React"
```

### 2. Cấu Hình OpenRouter API Key

Nếu bạn đã bỏ qua bước cấu hình API key trong wizard, cần cấu hình lại:

```bash
# Mở config editor
clawdbot config
```

Hoặc cấu hình trực tiếp:
```bash
# Set OpenRouter API key
clawdbot config set openrouter.apiKey "your-api-key-here"
```

**Lấy OpenRouter API Key:**
1. Truy cập: https://openrouter.ai/
2. Đăng ký/đăng nhập
3. Vào Settings → Keys
4. Create new key
5. Copy và paste vào lệnh trên

### 3. Kiểm Tra Cấu Hình
```bash
# Xem cấu hình hiện tại
clawdbot config show

# Kiểm tra model đã được set chưa
clawdbot config show models
```

### 4. Alternative: Dùng Dashboard Web

Nếu CLI không hoạt động, bạn có thể dùng Dashboard:
```
http://localhost:18789
```

Gateway đang chạy, bạn có thể chat trực tiếp qua web interface.

### 5. Thử Provider Khác

Nếu OpenRouter gặp vấn đề, chọn provider khác:
```bash
# Chọn Anthropic (Claude)
clawdbot config set model.provider anthropic
clawdbot config set anthropic.apiKey "your-anthropic-key"

# Hoặc OpenAI (ChatGPT)
clawdbot config set model.provider openai
clawdbot config set openai.apiKey "your-openai-key"
```

## Tóm Tắt

**Cách nhanh nhất:**
1. Mở Dashboard: http://localhost:18789
2. Chat trực tiếp qua web (không cần CLI)

**Hoặc:**
1. Cấu hình API key: `clawdbot config`
2. Dùng lệnh đúng: `clawdbot agent --agent --message "..."`
