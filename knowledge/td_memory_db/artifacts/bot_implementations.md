# Bot Implementation Patterns

The system supports running multiple bot roles simultaneously, each possibly on both Discord and Slack.

## 1. Multi-Role Initialization
`main.py` iterates over roles defined in `bot_roles.yaml` and checks for the existence of platform-specific tokens:
- Discord: `{ROLE_ID}_DISCORD_TOKEN`
- Slack: `{ROLE_ID}_SLACK_BOT_TOKEN` & `{ROLE_ID}_SLACK_APP_TOKEN`

Each bot instance is launched as an independent async task (Discord) or thread (Slack).

- **Slack Token Requirements**: For Socket Mode on a VPS, two tokens are required:
    - **`SLACK_BOT_TOKEN (xoxb)`**: Used for bot user identity, messaging, and channel interaction.
    - **`SLACK_APP_TOKEN (xapp)`**: Used by the Socket Mode handler to connect to the Slack WebSocket relay.


## 2. Discord Bot (discord.py)
- **Intents**: Requires `message_content` intent to read messages.
- **Message Listener**: `on_message` captures all messages from visible channels and saves them to the shared SQLite buffer.
- **Mention Handler**: If the bot is @mentioned, it calls the `QueryEngine` to generate an AI response.
- **Multi-Server**: A single bot token can serve multiple guilds; the buffer captures `guild_id` to keep context.

## 3. Slack Bot (Slack Bolt)
- **Socket Mode**: Used for self-hosting on VPS without exposed HTTP endpoints.
- **Threaded Replies**: Naturally uses Slack's threading for AI responses.
- **Event Listeners**:
    - `message` events: Capture raw logs to the buffer.
    - `app_mention` events: Trigger the memory-augmented Q&A flow.

## 4. Conversation Management
- **Integrated Intent Routing**: Mentions are routed through `IntentDetector` to decide between `QUERY`, `CREATE_TASK`, `UPDATE_TASK`, or `SET_REMINDER`.
- **Multi-turn Flow**: The `ConversationManager` handles the stateful step-by-step logic for complex tasks (like ClickUp task creation).
- **Instructional Prompts**: Bots ask for missing details (Title, Content, Deadline, Assignee) one by one and present a summary for final confirmation before execution.
- **Platform Specifics**: Slack uses threads for the entire flow, while Discord uses direct replies to maintain context.
- **Assignee @Mention Extraction**: When the bot asks "Who will be responsible?", it intercepts the user's reply. If the user @mentions someone:
    - **Discord**: Uses `message.mentions[0]` to get the user object.
    - **Slack**: Uses regex `r"<@([A-Z0-9]+)>"` to find the Slack ID and the WebClient to fetch the display name.
    - **Platform Normalization**: Stores the ID as `platform:user_id` to ensure unique identity across the system.

## 5. Slack Sync/Async Bridge
The Slack bot uses the `slack_bolt` framework, which is synchronous by default. To call the asynchronous `ClickUpClient`, `IntentDetector`, and `ConversationManager`, the system implements a `_run_async` helper:

```python
def _run_async(coro):
    """Run an async coroutine from a sync Slack Bolt handler."""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                future = pool.submit(asyncio.run, coro)
                return future.result(timeout=120)
        else:
            return loop.run_until_complete(coro)
    except RuntimeError:
        return asyncio.run(coro)
```

This pattern prevents event loop blocking and allows the bot to leverage async LLM and API calls while maintaining compatibility with the Bolt framework.
