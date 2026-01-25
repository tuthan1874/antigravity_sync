# Plan: Real-time Knowledge Sync (n8n to Open WebUI)

This plan describes how to automatically sync documents or data from n8n to Open WebUI's knowledge base (RAG) in real-time.

## Prerequisites
1. **Open WebUI API Key**: Go to `Settings > Account` in Open WebUI to generate an API Key.
2. **n8n Workflow**: An n8n instance capable of making HTTP requests.

## Proposed Architecture

```mermaid
graph LR
    Trigger[n8n Trigger: New File/Data] --> Upload[n8n: POST /api/v1/files/]
    Upload --> Knowledge[n8n: POST /api/v1/knowledge/{id}/file/add]
    Knowledge --> OpenWebUI[Open WebUI RAG Updated]
```

## Step-by-Step Implementation

### 1. Preparation in Open WebUI
- **Generate API Key**: Save this securely.
- **Find/Create Knowledge Base**: Navigate to the "Documents" or "Knowledge" section and create a collection. Note down the ID or name if needed.

### 2. n8n Workflow Configuration

#### Node 1: Trigger
- Use a trigger like **Google Drive (Watch Files)**, **Dropbox**, or a **Webhook** to receive the document in real-time.

#### Node 2: HTTP Request (Upload File)
- **Method**: `POST`
- **URL**: `https://chat.tdconsulting.vn/api/v1/files/`
- **Authentication**: Header `Authorization: Bearer YOUR_API_KEY`
- **Body Content Type**: `Multipart-form-data`
- **Data to Send**: The binary file from the trigger.
- **Output**: This will return a JSON object containing a `id` (this is the `file_id`).

#### Node 3: HTTP Request (Add to Knowledge - Optional)
- **Method**: `POST`
- **URL**: `https://chat.tdconsulting.vn/api/v1/knowledge/{knowledge_id}/file/add`
- **Authentication**: Header `Authorization: Bearer YOUR_API_KEY`
- **Body Content Type**: `JSON`
- **JSON Body**:
    ```json
    {
      "file_id": "{{$node[\"Upload File\"].json[\"id\"]}}"
    }
    ```

## Verification Plan
1. Trigger the n8n workflow with a test file.
2. Check the "Documents" or "Knowledge" section in Open WebUI to see if the file appears.
3. Chat with a model and verify it can reference the newly synced knowledge.
