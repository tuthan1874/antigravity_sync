# TD Games Memory Database System

Xây dựng hệ thống **Memory Database** cho công ty TD Games, sử dụng **Discord & Slack bots** (theo role: TD_CTO, TD_CEO, TD_PM, TD_HRM, TD_CFO...) để lắng nghe tin nhắn trên các channel, chuẩn hoá dữ liệu qua **mem0**, lưu vào **Qdrant** (self-hosted). Mỗi bot có collection riêng. Hỗ trợ **daily digest** thay vì lưu realtime để tránh data rác.

---

## User Review Required

> [!IMPORTANT]
> **Lựa chọn LLM Provider**: Hệ thống cần 1 LLM để mem0 trích xuất facts và tạo embeddings. mem0 hỗ trợ: OpenAI, Gemini, OpenRouter, Ollama. Bạn muốn dùng provider nào? (Đề xuất: **Gemini** hoặc **OpenRouter** vì công ty đã có kinh nghiệm).

> [!IMPORTANT]
> **Qdrant đã có sẵn chưa?** Cần biết URL và port của Qdrant VPS hiện tại (ví dụ: `http://vps-ip:6333`). Nếu chưa có, plan sẽ bao gồm cài đặt Qdrant.

> [!IMPORTANT]
> **Danh sách Bot Roles**: Xác nhận danh sách các bot role cần tạo. Dự kiến: `TD_CTO`, `TD_CEO`, `TD_PM`, `TD_HRM`, `TD_CFO`. Có thêm role nào khác không?

> [!WARNING]
> **Discord Bot Tokens & Slack App Tokens**: Mỗi bot role cần 1 Discord Bot Token riêng và 1 Slack App riêng (hoặc dùng chung 1 app với nhiều identity). Bạn muốn:
> - **(A)** Mỗi role = 1 Discord App + 1 Slack App riêng biệt (nhiều token, quản lý phức tạp hơn)
> - **(B)** 1 Discord App + 1 Slack App chung, xử lý multi-role bằng prefix/config (đơn giản hơn, 1 bot respond với các persona khác nhau)

---

## Architecture Overview

```mermaid
graph TB
    subgraph "Chat Platforms"
        DC[Discord Channels]
        SL[Slack Channels]
    end

    subgraph "Bot Layer (Python)"
        DB[Discord Bot - discord.py]
        SB[Slack Bot - slack-bolt]
    end

    subgraph "Message Buffer"
        BUF[(SQLite/JSON Buffer<br/>Raw Messages per Day)]
    end

    subgraph "Daily Digest Engine"
        SCH[APScheduler / Cron]
        LLM[LLM Provider<br/>Gemini/OpenRouter]
        M0[mem0 Memory Layer]
    end

    subgraph "Vector Store (VPS)"
        Q1[(Qdrant: td_cto)]
        Q2[(Qdrant: td_ceo)]
        Q3[(Qdrant: td_pm)]
        Q4[(Qdrant: td_hrm)]
        Q5[(Qdrant: td_cfo)]
    end

    DC --> DB
    SL --> SB
    DB --> BUF
    SB --> BUF
    SCH -->|"Daily 23:00"| LLM
    LLM --> M0
    M0 --> Q1 & Q2 & Q3 & Q4 & Q5

    DC -.->|"@bot mention"| DB
    SL -.->|"@bot mention"| SB
    DB -.->|"Query"| M0
    SB -.->|"Query"| M0
    M0 -.->|"Search"| Q1 & Q2 & Q3 & Q4 & Q5
```

### Data Flow

1. **Lắng nghe (Listen)**: Bot join channel → ghi nhận mọi tin nhắn vào **buffer** (SQLite hoặc JSON file, theo ngày)
2. **Daily Digest (23:00)**: Scheduler trigger → LLM đọc buffer ngày hôm đó → tổng hợp thông tin quan trọng → mem0 chuẩn hoá → lưu vào Qdrant collection tương ứng
3. **Query (@mention)**: User tag bot → bot tìm kiếm trên Qdrant collection của mình → LLM generate câu trả lời → reply

---

## Proposed Changes

### Project Structure

```
Sync_Qdrant/
├── .env.example                  # Environment variables template
├── .env                          # Actual env vars (gitignored)
├── requirements.txt              # Python dependencies
├── docker-compose.yml            # Docker setup for deployment
├── Dockerfile                    # Production container
├── config/
│   ├── __init__.py
│   ├── settings.py               # Pydantic settings management
│   └── bot_roles.yaml            # Bot role definitions
├── core/
│   ├── __init__.py
│   ├── memory_engine.py          # mem0 + Qdrant integration
│   ├── message_buffer.py         # SQLite buffer for daily messages
│   ├── daily_digest.py           # LLM summarization + mem0 storage
│   └── query_engine.py           # Search & answer generation
├── bots/
│   ├── __init__.py
│   ├── discord_bot.py            # Discord bot implementation
│   └── slack_bot.py              # Slack bot implementation
├── scheduler/
│   ├── __init__.py
│   └── jobs.py                   # APScheduler job definitions
├── main.py                       # Entry point - starts all bots + scheduler
└── scripts/
    ├── setup_qdrant_collections.py  # One-time setup script
    └── migrate_buffer.py            # Utility to manually process buffer
```

---

### Config Management

#### [NEW] [.env.example](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/.env.example)

```env
# LLM Provider
LLM_PROVIDER=gemini                    # gemini | openrouter | ollama | openai
LLM_MODEL=gemini-2.0-flash
LLM_API_KEY=your_api_key_here

# Embedder
EMBEDDER_PROVIDER=gemini               # gemini | openai | ollama
EMBEDDER_MODEL=models/text-embedding-004

# Qdrant
QDRANT_HOST=your-vps-ip
QDRANT_PORT=6333
QDRANT_API_KEY=                        # Optional, if Qdrant has auth

# Discord
DISCORD_BOT_TOKEN=your_discord_bot_token

# Slack
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_APP_TOKEN=xapp-your-slack-app-token
SLACK_SIGNING_SECRET=your_signing_secret

# Digest Schedule
DIGEST_CRON_HOUR=23
DIGEST_CRON_MINUTE=0
DIGEST_TIMEZONE=Asia/Ho_Chi_Minh
```

#### [NEW] [bot_roles.yaml](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/config/bot_roles.yaml)

Định nghĩa các role và collection tương ứng:

```yaml
roles:
  TD_CTO:
    collection_name: "td_cto_memory"
    description: "Chief Technology Officer - Technical decisions, architecture, tech stack"
    system_prompt: "You are TD_CTO, the Chief Technology Officer of TD Games..."
    
  TD_CEO:
    collection_name: "td_ceo_memory"
    description: "Chief Executive Officer - Strategy, vision, business decisions"
    system_prompt: "You are TD_CEO, the CEO of TD Games..."
    
  TD_PM:
    collection_name: "td_pm_memory"
    description: "Project Manager - Project tracking, timelines, task management"
    system_prompt: "You are TD_PM, the Project Manager of TD Games..."
    
  TD_HRM:
    collection_name: "td_hrm_memory"
    description: "HR Manager - People, hiring, culture, team management"
    system_prompt: "You are TD_HRM, the HR Manager of TD Games..."
    
  TD_CFO:
    collection_name: "td_cfo_memory"
    description: "Chief Financial Officer - Finance, budget, revenue, costs"
    system_prompt: "You are TD_CFO, the CFO of TD Games..."
```

---

### Core Memory Engine

#### [NEW] [memory_engine.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/memory_engine.py)

- Khởi tạo `mem0.Memory` instance cho mỗi role với cấu hình Qdrant riêng
- Mỗi role có `collection_name` riêng trong Qdrant
- Cung cấp methods: `add_memory()`, `search_memory()`, `get_all_memories()`

```python
# Pseudo-code
from mem0 import Memory

class MemoryEngine:
    def __init__(self, role_config):
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": QDRANT_HOST,
                    "port": QDRANT_PORT,
                    "collection_name": role_config["collection_name"],
                }
            },
            "llm": {
                "provider": LLM_PROVIDER,
                "config": {"model": LLM_MODEL, "api_key": LLM_API_KEY}
            },
            "embedder": {
                "provider": EMBEDDER_PROVIDER,
                "config": {"model": EMBEDDER_MODEL}
            }
        }
        self.memory = Memory.from_config(config)
    
    def add(self, messages, user_id, metadata=None):
        return self.memory.add(messages, user_id=user_id, metadata=metadata)
    
    def search(self, query, user_id=None, limit=5):
        return self.memory.search(query, user_id=user_id, limit=limit)
```

#### [NEW] [message_buffer.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/message_buffer.py)

- SQLite database lưu raw messages theo ngày
- Schema: `id, platform, channel_id, channel_name, user_id, username, content, timestamp, role_tag, processed`
- Methods: `save_message()`, `get_unprocessed_by_date()`, `mark_processed()`

#### [NEW] [daily_digest.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/daily_digest.py)

- Đọc messages chưa processed từ buffer
- Nhóm theo role (dựa trên channel mapping hoặc tag)
- Gọi LLM tổng hợp: *"Summarize the key decisions, action items, and important information from these messages"*
- Dùng mem0 `add()` để chuẩn hoá và lưu vào Qdrant

#### [NEW] [query_engine.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/core/query_engine.py)

- Nhận query từ user mention
- Search Qdrant collection tương ứng qua mem0
- Generate câu trả lời dùng LLM với context từ memories
- Return formatted response

---

### Discord Bot

#### [NEW] [discord_bot.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/bots/discord_bot.py)

- Dùng `discord.py` với `Message Content Intent` enabled
- **on_message**: Ghi mọi tin nhắn vào buffer (trừ bot messages)
- **on_message (mention)**: Khi user `@TD_CTO question?` → gọi `query_engine` → reply
- Hỗ trợ slash commands: `/ask_cto`, `/ask_ceo`... (optional)
- Xác định role dựa trên bot mention hoặc channel mapping

```python
# Key flow
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    # Save to buffer
    buffer.save_message(platform="discord", ...)
    
    # Check if bot is mentioned
    if bot.user.mentioned_in(message):
        role = determine_role(message)
        answer = await query_engine.answer(
            query=message.content,
            role=role
        )
        await message.reply(answer)
```

### Slack Bot

#### [NEW] [slack_bot.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/bots/slack_bot.py)

- Dùng `slack-bolt` Python SDK với Socket Mode
- **message event**: Ghi mọi tin nhắn vào buffer
- **app_mention event**: Khi user `@TD_CTO question?` → gọi `query_engine` → reply

```python
# Key flow
@app.event("message")
def handle_message(event, say):
    buffer.save_message(platform="slack", ...)

@app.event("app_mention")
def handle_mention(event, say):
    role = determine_role(event)
    answer = query_engine.answer(query=event["text"], role=role)
    say(answer, thread_ts=event["ts"])
```

---

### Scheduler

#### [NEW] [jobs.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/scheduler/jobs.py)

- Dùng `APScheduler` với `CronTrigger`
- Job chạy lúc 23:00 VN time hàng ngày
- Gọi `daily_digest.process_day()` cho từng role
- Logging kết quả

---

### Main Entry Point

#### [NEW] [main.py](file:///e:/TDC_App/TDGAMES_App/Sync_Qdrant/main.py)

- Load config từ `.env` và `bot_roles.yaml`
- Khởi tạo: Buffer DB, Memory Engines, Query Engines
- Start Discord bot (asyncio)
- Start Slack bot (threading hoặc asyncio)
- Start APScheduler
- Graceful shutdown handling

---

## Tech Stack Summary

| Component | Technology | Version |
|-----------|-----------|---------|
| Language | Python | 3.11+ |
| Discord | discord.py | 2.x |
| Slack | slack-bolt | 1.x |
| Memory Layer | mem0ai | latest |
| Vector DB | Qdrant | self-hosted |
| LLM | Gemini / OpenRouter | configurable |
| Buffer DB | SQLite | built-in |
| Scheduler | APScheduler | 3.x |
| Config | pydantic-settings | 2.x |
| Deployment | Docker + docker-compose | - |

## Dependencies (`requirements.txt`)

```
mem0ai
discord.py
slack-bolt
slack-sdk
apscheduler
pydantic-settings
pyyaml
python-dotenv
aiohttp
```

---

## Verification Plan

### Automated Tests

1. **Unit test memory_engine.py**:
   ```bash
   python -m pytest tests/test_memory_engine.py -v
   ```
   - Test khởi tạo mem0 với config Qdrant
   - Test add/search memory (mock Qdrant)

2. **Unit test message_buffer.py**:
   ```bash
   python -m pytest tests/test_buffer.py -v
   ```
   - Test save/retrieve messages
   - Test mark_processed

3. **Unit test daily_digest.py**:
   ```bash
   python -m pytest tests/test_digest.py -v
   ```
   - Test summarization flow (mock LLM)

### Manual Verification

1. **Setup Qdrant**: Verify Qdrant collections are created correctly via Qdrant Dashboard (`http://vps-ip:6333/dashboard`)
2. **Discord Test**: 
   - Invite bot vào test channel
   - Gửi vài tin nhắn → kiểm tra buffer SQLite có ghi nhận
   - Tag bot `@TD_CTO test question` → kiểm tra có trả lời
3. **Slack Test**:
   - Invite bot vào test channel
   - Gửi vài tin nhắn → kiểm tra buffer
   - Tag bot `@TD_CTO test question` → kiểm tra reply
4. **Daily Digest Test**:
   - Chạy manual: `python -m scripts.manual_digest --date today`
   - Verify dữ liệu đã lưu vào Qdrant collection

> [!TIP]
> Có thể bắt đầu với 1 role (TD_CTO) để test toàn bộ flow trước, sau đó mở rộng cho các role khác chỉ cần thêm config vào `bot_roles.yaml`.
