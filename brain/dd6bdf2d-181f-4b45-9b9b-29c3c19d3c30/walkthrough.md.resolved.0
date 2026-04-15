# ZaloCRM Deployment Walkthrough

We have successfully fully deployed the ZaloCRM application to your Megahost_02 VPS.

## Changes Made

### 1. ZaloCRM Code Setup
- Cloned the repository from [locphamnguyen/ZaloCRM](https://github.com/locphamnguyen/ZaloCRM) into `/opt/ZaloCRM`.
- Generated secure cryptographic keys for `JWT_SECRET` and `ENCRYPTION_KEY`.
- Set up a secure database password for the PostgreSQL container and wrote the configuration to `/opt/ZaloCRM/.env`.

### 2. Docker Services Configuration
- Built the containers using `docker compose up -d --build`. This spun up:
  - `zalo-crm-db`: PostgreSQL 16
  - `zalo-crm-app`: Node.js FastAPI app mapped to port `3080`.
  - `zalo-crm-backup`: Local pgdump backups.

### 3. Nginx Reverse Proxy & WebSockets
- Created a configuration file at `/etc/nginx/sites-available/zalo.tdconsulting.vn` that correctly routes traffic to port `3080`.
- Handled WebSocket connection upgrades to ensure the realtime chat capabilities of ZaloCRM work reliably.

### 4. SSL Encryption
- Requested and provisioned Let's Encrypt certificates using the `tdconsultingvn@gmail.com` email for automated renewals.
- Secured the endpoint behind an HTTPS proxy via Certbot.

## Validation Results
- The Docker build was successful and all 3 containers are healthy and running via Docker Compose.
- Nginx restart succeeded without configuration issues.
- Certbot successfully secured the domain.

> [!TIP]
> You can now access your application securely at: **https://zalo.tdconsulting.vn**
> For your first run, you should access the dashboard to create the administrator account and start linking your Zalo accounts.
