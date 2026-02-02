# App Preview & Feedback Platform - Implementation Plan

## Goal Description
Build a web application for previewing and providing direct vector-based feedback on Art (PSD) and Animation (Spine 2D) deliverables. The app will feature realtime collaboration, project organization, and a premium "Neomorphism" or modern aesthetic.

## Tech Stack & Architecture
- **Frontend**: Next.js (App Router), React, TailwindCSS, Framer Motion (animations).
- **State/Logic**: React Server Components (RSC) for data fetching, Client Components for interaction.
- **Visuals**: Konva.js (Vector Drawing), ag-psd (PSD Parsing), spine-web-player (4.2+).
- **Backend/Infra**: Supabase (Postgres, Auth, Realtime), Cloudflare R2 (Storage).
- **Design System**: Custom premium UI based on `web-design-guidelines` skill.

## Proposed Changes & Phasing

### Phase 1: Foundation & Infrastructure
**Goal**: Set up the project shell, database, and storage.
- **Frontend**:
    - Initialize Next.js app with `create-next-app`.
    - Configure TailwindCSS with a custom premium palette (dark mode focused).
    - Setup generic layout with Sidebar/Header.
- **Backend (Supabase)**:
    - Tables: `projects`, `assets` (discriminator for 'psd' vs 'spine'), `comments`, `annotations` (vector paths).
    - RLS Policies for secure access.
- **Storage (R2)**:
    - Bucket structure: `/{projectId}/{assetId}/...`

### Phase 2: Core UI & Project Management
**Goal**: Users can log in, create projects, and upload files.
- **Auth**: Supabase Auth integration (Login/Signup pages).
- **Dashboard**:
    - Project Grid/List view with sleek cards.
    - specialized "Upload Dropzone" handling distinct file types (.psd vs .json/.atlas/.png for Spine).
- **Navigation**: Client-side routing for seamless transitions.

### Phase 3: The Art Module (PSD Focus)
**Goal**: View PSDs and toggle layers.
- **Viewer Component**:
    - Use `ag-psd` to parse uploaded PSDs in the browser (or Edge Function if too large).
    - Render layers to Canvas or HTML elements.
    - Layer Control Panel: Toggle visibility, opacity.
- **Feedback Layer (Konva.js)**:
    - Overlay a transparency-friendly Konva Stage on top of the art.
    - Tools: Pen (Vector lines), Arrow, Circle.

### Phase 4: The Animation Module (Spine Focus)
**Goal**: Play Spine animations and draw on specific frames.
- **Spine Player Integration**:
    - Wrap `spine-web-player` in a React component (`SpinePlayerWrapper`).
    - Expose controls: `play`, `pause`, `setAnimation`, `seek`.
- **Frame-Synced Feedback**:
    - The Drawing Canvas must track the current animation "time" or "frame".
    - Store annotations with a `timestamp` or `frameIndex`.
    - When playback stops, show annotations for that timestamp. When playing, hide them (or show ghosting).

### Phase 5: Realtime Collaboration
**Goal**: Multiplayer experience.
- **Presence**: Show who is viewing the project (avatars).
- **Live Cursors**: Track mouse movements using Supabase Realtime Broadcast.
- **Live Drawing**: Broadcast vector path addition/modification events to other connected clients.

## Verification Plan
### Automated Tests
- Unit tests for utility functions (e.g., coordinate conversion).
- E2E tests for the critical path: Login -> Create Project -> Upload -> View.

### Manual Verification
1. **PSD Loading**: Verify complex PSDs load with correct layer structure.
2. **Spine Playback**: Ensure animations play smoothly and transparency works.
3. **Drawing Sync**: Open two windows, draw in one, verify instant appearance in second.
