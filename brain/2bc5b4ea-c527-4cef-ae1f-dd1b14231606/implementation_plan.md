# Plan: Install Open WebUI

This plan outlines the steps to install and run Open WebUI on your system using Docker. Since you don't have Ollama installed yet, we will use the bundled Ollama image which includes both Open WebUI and Ollama in a single container.

## Proposed Changes

### Environment Setup
- Verify Docker is running (already confirmed).
- Create a persistent data volume for Open WebUI and Ollama.

### Installation Steps
We will use the following Docker command to start Open WebUI with bundled Ollama.

#### Option 1: CPU Only (Recommended for initial setup)
```bash
docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

#### Option 2: GPU Support (Requires Nvidia Container Toolkit)
If you have the Nvidia Container Toolkit installed on your WSL/Linux system, you can use:
```bash
docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

## Verification Plan

### Automated Steps
- Check container status: `docker ps`
- Verify logs for any errors: `docker logs open-webui`

### Manual Verification
1. Open [http://localhost:3000](http://localhost:3000) in your browser.
2. Sign up (the first user created is the admin).
3. Verify that you can pull a model (e.g., `llama3`) and start a chat.
