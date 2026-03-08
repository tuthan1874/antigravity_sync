# Reminder & Cron System

The system includes a persistent reminder engine that allows users to set one-time or recurring notifications via chat.

## Architecture
- **Storage**: Reminders are stored in a SQLite table `reminders` with fields for `role_id`, `user_id`, `platform`, `message`, `scheduled_time`, and `repeat_type`.
- **Scheduler**: Uses `APScheduler` (AsyncIOScheduler) to trigger events.
- **Resilience**: On application startup, the `ReminderManager` loads all active reminders from SQLite and re-adds them to the scheduler.

## Reminder Types
- **Once**: Fires once at the specified time and deactivates.
- **Daily**: Fires every day at the same hour/minute.
- **Weekly**: Fires on the same day of the week and time.

## Workflow
1. User tags bot: "Nhac toi hop luc 2h chieu mai".
2. Intent Detector catches `SET_REMINDER`.
3. Conversation Manager clarifies contents/time.
4. Reminder Manager adds to DB and schedules job.
5. At trigger time, a callback is executed that sends a direct @mention message to the original discord/slack channel with the reminder text.
