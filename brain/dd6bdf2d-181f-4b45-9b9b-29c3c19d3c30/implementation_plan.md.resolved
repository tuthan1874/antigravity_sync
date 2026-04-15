# Deploy ZaloCRM to Megahost_02

Domain `zalo.tdconsulting.vn` already resolves to the correct IP of Megahost_02 (`180.93.144.98`), so we are ready to proceed.

## User Review Required

> [!IMPORTANT]
> The default ZaloCRM deployment runs on port `3080`. This port needs to be conflict-free on your VPS. We also assuming you want to deploy the application in `/opt/ZaloCRM` folder.
> Please review the `.env` settings. Specifically, you will be prompted to change or verify the admin password / secret keys after the first run, but we will initiate it with default/random secure ones for `JWT_SECRET`, etc. if applicable. 

## Proposed Changes

### 1. ZaloCRM Application Setup (Docker)
- We will clone the `ZaloCRM` repository to `/opt/ZaloCRM` on `Megahost_02`.
- Copy `.env.example` to `.env` and set up any necessary keys.
- Run `docker compose up -d --build` to deploy the application containers. The web interface will bind locally to `127.0.0.1:3080`.

### 2. Nginx Reverse Proxy Configuration
- Create a new Nginx server block for `zalo.tdconsulting.vn` at `/etc/nginx/sites-available/zalo.tdconsulting.vn`.
- Explicitly add WebSocket headers (Upgrade, Connection "upgrade") to `proxy_pass` to support ZaloCRM's `Socket.IO` requirement.
- Enable the site via `/etc/nginx/sites-enabled/` and reload Nginx.

### 3. SSL Configuration (Certbot)
- Run Certbot with the `--nginx` plugin to automatically provision Let's Encrypt certificates for `zalo.tdconsulting.vn` and configure redirect from HTTP to HTTPS.

## Open Questions

> [!WARNING]
> Certbot usually requires an email address for important expiry notifications. Can I use `tdconsultingvn@gmail.com` as the Let's Encrypt registration email?

## Verification Plan

### Automated Tests
- We'll run `docker ps` to verify the ZaloCRM containers are healthy.
- `nginx -t` to check syntax.
- View Logs of ZaloCRM server if there's any startup issue.

### Manual Verification
- Access `https://zalo.tdconsulting.vn` from your browser.
- Verify the WebSockets and backend are fully working by attempting a login.
