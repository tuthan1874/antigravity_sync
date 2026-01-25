# Implementation Plan - Portfolio Animation Spine Website

This project aims to create a professional portfolio website for showcasing Spine animations. It will run entirely client-side, using IndexedDB for persistent storage of large animation files (images/atlases).

## User Review Required
> [!IMPORTANT]
> **Spine Runtime License**: Ensure you have the right to use the Spine Web Player or runtime in a public portfolio. This plan assumes we will use a compatible runtime or the official Spine Web Player.

> [!NOTE]
> **Storage Limits**: IndexedDB has generous limits, but storing many large PNGs/JSONs might eventually hit browser quota limits.

## Proposed Changes

### Tech Stack
- **Framework**: React (Vite)
- **Styling**: Tailwind CSS (with `clsx`, `tailwind-merge`)
- **Icons**: Lucide React
- **Storage**: `idb-keyval` (Simple Promise-based IndexedDB wrapper)
- **File Handling**: `jszip` (For parsing uploaded Spine exports)
- **Routing**: `react-router-dom`

### Architecture

#### Data Model (IndexedDB)
We will store "Projects". A Project consists of:
- `id`: UUID
- `name`: String
- `thumbnail`: Blob (generated or first frame)
- `files`: Object containing the raw Blobs for `.json`, `.atlas`, and `.png` files.

#### Directory Structure
```
src/
  components/
    common/       # Button, Card, Modal, Input
    layout/       # Sidebar, Header
    features/
      upload/     # Dropzone, Progress
      gallery/    # ProjectGrid, ProjectCard
      viewer/     # SpinePlayerWrapper
  services/
    storage.ts    # IndexedDB logic
    parser.ts     # Zip file parsing and validation
  hooks/
    useProjects.ts
    useSpinePlayer.ts
  types/
    index.ts
  App.tsx
  main.tsx
```

### Key Features

#### 1. Upload & Parsing
- User uploads a `.zip` file containing Spine exports.
- System unzips and looks for matching triplets: `name.json` (or .skel), `name.atlas`, `name.png`.
- Validates that all necessary files for a skeleton are present.
- Saves valid sets to IndexedDB.

#### 2. Gallery View
- Displays a grid of uploaded projects.
- Shows thumbnails (if possible to generate, otherwise a placeholder).
- Allows deleting projects.

#### 3. Viewer
- A dedicated view to render the Spine animation.
- Controls: Animation list selection, Skin selection, Play/Pause, Zoom/Pan.

## Verification Plan

### Automated Tests
- N/A for this rapid prototype, but we will ensure the build passes.

### Manual Verification
1. **Upload Flow**: Upload a valid Spine ZIP file. Verify it appears in the gallery.
2. **Persistence**: Refresh the page. Verify the project is still there.
3. **Playback**: Open the project. Verify the animation plays and controls work.
4. **Error Handling**: Upload an invalid ZIP. Verify appropriate error messages.
