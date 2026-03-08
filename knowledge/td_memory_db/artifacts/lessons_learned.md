# Best Practices & Lessons Learned

## 1. Sync/Async Interoperability (Slack Bolt)
A major challenge was the synchronous nature of the `slack_bolt` framework when hosted in Socket Mode. The system needed to call asynchronous `ClickUpClient`, `IntentDetector`, and `ConversationManager` methods.

**Best Practice**: Use a robust `_run_async` helper that handles existing event loops and thread pools:

```python
def _run_async(coro):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                future = pool.submit(asyncio.run, coro)
                return future.result()
        else:
            return loop.run_until_complete(coro)
    except RuntimeError:
        return asyncio.run(coro)
```

## 2. Integration Auto-Provisioning (ClickUp)
To reduce manual setup friction, the system implements a "Find or Create" flow for integrations.

**Best Practice**: 
- **Fixed Infrastructure**: Use environment variables for IDs that shouldn't change (e.g., `CLICKUP_FOLDER_ID`).
- **Dynamic Discovery**: Auto-create lists and custom fields based on dynamic role configurations.
- **Persistence**: Save discovered/created IDs (like `list_id`) back to a persistent YAML config to avoid redundant API calls on restart.

## 3. Dark OLED Design System
An OLED-optimized theme provides high contrast and a professional "SaaS-ready" aesthetic.

**Standard**:
- **Background**: `#020617` (Deep slate/black).
- **Accents**: `#22C55E` (Emerald/Green).
- **Glassmorphism**: Use translucent borders (`border: 1px solid rgba(255, 255, 255, 0.1)`) instead of heavy backgrounds for cards.
- **Typography**: `Fira Code` for technical text/IDs; `Fira Sans` for UI labels.

## 4. Multi-turn Conversation Management
Complex platform operations (like task creation) are fragile if done in a single message.

**Strategy**:
- **Intent Discovery**: Use an LLM to extract as much info as possible from the initial message.
- **Stateful Progression**: Track the conversation step (e.g., [1/5]) in a SQLite database to persist through restarts.
- **Confirmation Loop**: Always show a "Ready to Create" summary and wait for an explicit "OK" to avoid unintended API side-effects.

## 5. Message Buffering for RAG
For daily digests (summarization), buffering messages by date provides:
- **Resilience**: Bot downtime doesn't mean message loss (capture -> buffer is fast).
- **Efficiency**: Allows batching multiple messages into a single LLM call for summarization.
- **Context**: Keeps channel-specific threads together for better summarization accuracy.
53: 
54: ## 6. Cross-Platform User Identity
55: User IDs differ between Discord and Slack. To maintain a consistent identity in ClickUp tasks:
56: 
57: **Best Practice**: Prefix the ID with the platform name (`discord:{id}`, `slack:{id}`). This gives the reminder engine the context it needs to send notifications to the correct platform using the appropriate bot roll.
