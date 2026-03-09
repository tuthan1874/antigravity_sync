# Scheduled Digest Cron Upgrades
- [x] Upgrade `core/scheduled_digest.py` — full cron expression, timezone, callback wiring
- [x] Update `core/intent_detector.py` — extract cron expression from natural language
- [x] Update `bots/discord_bot.py` — wire callback to post digest back to channel
- [x] Update `bots/slack_bot.py` — wire callback to post digest back to channel
- [x] Update `main.py` — pass digest + buffer to create the callback
- [x] Add `get_messages_by_date()` to `core/message_buffer.py`
- [x] Verify all files parse correctly
