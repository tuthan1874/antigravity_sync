# Conversational Logic & Intent Detection

To support task management and reminders, the system uses a two-stage approach to process @mentions.

## 1. Intent Detection
Before responding, the bot uses an LLM (`core/intent_detector.py`) to classify the user's message into one of four intents.

### Classification Logic
The system prompt instructs the LLM to identify specific Vietnamese keywords and patterns:

- **QUERY**: General questions or info requests ("hoi", "cho biet").
- **CREATE_TASK**: Action items or assignments ("tao task", "assign", "phan cong").
- **UPDATE_TASK**: Updates to existing work ("xong roi", "hoan thanh", "doi deadline").
- **SET_REMINDER**: Specific time-based alerts ("nhac toi", "nhac hen", "reminder").

### Structured Extraction
The LLM returns a JSON object containing the intent name and extracted parameters:

```json
{
  "intent": "CREATE_TASK",
  "confidence": 0.95,
  "extracted_info": {
    "task_name": "Fix landing page button",
    "description": "Button is not clickable on mobile",
    "assignee": "dangt",
    "deadline": "tomorrow 2pm"
  }
}
```

This allows the system to pre-fill parts of the conversational flow, speeding up user interaction.

## 2. Multi-turn Conversation Manager
If a task or reminder intent is detected, the `ConversationManager` (`core/conversation_manager.py`) takes over.

### State Machine
- **State Storage**: Conversations are tracked per User + Channel in a SQLite database and in-memory cache.
- **Timeouts**: Conversations auto-cancel after 10 minutes of inactivity.
- **Flow Engine**:
  1. Detect intent and extract initial parameters from the @mention request.
  2. Sequential Progression: Ask remaining questions one by one (e.g., "Ten task la gi?").
  3. **Auto-Skipping**: Steps that are pre-filled by the intent detector are automatically skipped.
  4. **Platform-Aware Assignees**: The bot intercepts replies to the "assignee_name" step. If the message contains an @mention, it extracts the display name and platform ID (e.g., `discord:123` or `slack:UABC`). Otherwise, it uses the requester's platform prefix for the ID.
  5. Confirmation Summary: Show a full summary (Task Name, Description, Assignee Name/ID, Dates).
  6. Wait for explicit "OK" or Vietnamese affirmation ("duoc", "tao di") before calling the ClickUp API.

### Natural Language Date Parsing
The manager uses a specialized LLM prompt to parse Vietnamese temporal expressions (e.g., "sang thu hai tuan sau") into valid ISO datetime strings based on the current system time.
