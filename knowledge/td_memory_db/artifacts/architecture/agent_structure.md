# Agent Folder Structure & Memory Layers (Proposed)

Based on the [OpenClaw](https://github.com/nextlevelbuilder/openclaw) agent model, the system is evolving towards a more structured organization for bot personas and persistent context.

## 1. Directory Structure

Each bot role (agent) is proposed to have its own configuration directory within `data/agents/{role_id}/`:

| File | Purpose |
|------|---------|
| `SOUL.md` | **Persona / Rules**: The agent's tone, decision-making principles, and safety rules. The core identity. |
| `IDENTITY.md` | **Identification**: Display name, role description, vibe, and representative emoji. |
| `AGENTS.md` | **Scope**: Mission statement and what the agent specifically focuses on (e.g., CTO focuses on architecture). |
| `USER.md` | **Human Context**: Preferences for the user (Toan), such as timezone, address language, and style. |
| `MEMORY.md` | **Fixed Memory (Layer B)**: Durable business context, standards, and historical decisions in Markdown format. |
| `memory/*.md` | **Memory Chunks**: Subject-specific context that is too large for `MEMORY.md`. |
| `TOOLS.md` | **Tool Config**: Instructions or configs for tools used by that specific agent. |

## 2. Three-Layer Memory Model

To provide the most accurate and context-aware responses, the bots utilize three distinct layers of memory:

### Layer A: Session Context (Short-Term)
- **What**: Conversation history in the current chat session.
- **Persistence**: Temporary, limited by the model's context window.
- **Usage**: Handles follow-up questions and immediate thread context.

### Layer B: Workspace Memory (Medium-Term / File-Based)
- **What**: Content from `MEMORY.md` and `memory/*.md` in the agent's folder.
- **Persistence**: Durable and easily editable by humans.
- **Usage**: Injected into the **System Prompt** every time. Contains rules, company standards, and "facts" that shouldn't rely on semantic search.

### Layer C: Long-Term Memory (Persistent / Vector Search)
- **What**: Mem0-managed storage in **Qdrant**.
- **Persistence**: Indefinite. Collections are scoped to each bot role.
- **Usage**: RAG (Retrieval-Augmented Generation). The agent searches for relevant facts from past chat history or summarized digests when the user asks a question.

## 3. Benefits of this Architecture
- **Isolation**: Each bot has its own "brain" folder, making it easier to clone or customize roles.
- **Persona Depth**: Moving beyond a single line in `bot_roles.yaml` to a multi-page `SOUL.md` allows for much richer character interaction.
- **Contextual Accuracy**: Layer B ensures the bot never "forgets" foundational company rules, even if they aren't semantically identical to the user's query.
- **Maintainability**: Markdown files are easier to manage and version control than database records for persona definition.
