# Walkthrough: Open WebUI Installation

I have successfully installed Open WebUI using Docker with bundled Ollama support.

## Changes Made
- Pulled the `ghcr.io/open-webui/open-webui:ollama` Docker image.
- Started a Docker container named `open-webui` with the following configuration:
  - Port `3000` on host mapped to `8080` in container.
  - Persistent volumes for Ollama (`ollama`) and Open WebUI (`open-webui`).
  - Auto-restart enabled.

## Verification Results

### Container Status
The container is up and running:
```bash
CONTAINER ID   IMAGE                                COMMAND                  STATUS          PORTS
cc9cd5e171fa   ghcr.io/open-webui/open-webui:ollama "/app/backend/start.…”   Up 2 minutes    0.0.0.0:3000->8080/tcp
```

### Server Logs
The server has started successfully:
```text
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

## How to Use
1. Open your browser and go to [http://localhost:3000](http://localhost:3000).
2. Create your admin account (first user registered).
3. In the settings/models section, you can pull models like `llama3` to start chatting.
