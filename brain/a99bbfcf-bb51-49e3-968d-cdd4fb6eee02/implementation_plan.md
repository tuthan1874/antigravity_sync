# Spine 2D Preview App Implementation Plan

## Goal Description
Build a client-side web application to upload and preview Spine 2D animations using React, Vite, and TypeScript, as specified in the README.md.

## Proposed Changes
We will scaffold a new Vite project and verify the following structure:

### Project Root
- [NEW] All Vite config files (vite.config.ts, tsconfig.json, etc.)
- [NEW] package.json

### src/
#### Infrastructure
- [NEW] `spine/types.ts`: Shared types not directly in spine-webgl
- [NEW] `spine/SpineRuntime.ts`: Wrapper around spine-webgl for loading and state management
- [NEW] `spine/SpineRenderer.ts`: WebGL rendering logic using spine-webgl

#### React Integration
- [NEW] `hooks/useSpinePlayer.ts`: Hook to bridge React components with `SpineRuntime`

#### UI Components
- [NEW] `components/FileUpload.tsx`: Handle ZIP uploads
- [NEW] `components/AnimationSelector.tsx`: Dropdown for animations
- [NEW] `components/PlaybackControls.tsx`: Play, pause, loop controls
- [NEW] `components/ViewControls.tsx`: Zoom and pan
- [NEW] `components/BackgroundControls.tsx`: Background color/image settings
- [NEW] `components/ExportControls.tsx`: Export settings (width, height, format, record button)

### Interaction & Layout
- [MODIFY] `hooks/useSpinePlayer.ts`: Add listener for recording frames (if needed) or expose canvas for external recorder.
- [MODIFY] `App.tsx`: Integrate ExportControls. Logic for `MediaRecorder` (MP4/WebM) and `gif.js` (GIF).
- [MODIFY] `components/ExportControls.tsx`: Add Width/Height inputs that update the `canvas-wrapper` size.

### Dependencies
- `gif.js` (for GIF export)
- `file-saver` (optional, for saving files easily)

### Interaction & Layout
- [MODIFY] `hooks/useSpinePlayer.ts`: Add mouse event listeners for pan (right-click) and zoom (scroll).
- [MODIFY] `App.tsx`: Implement resizable container logic and background image handling.
- [MODIFY] `components/BackgroundControls.tsx`: Add file input for background upload.

#### Main App
- [NEW] `App.tsx`: Layout and state orchestration
- [NEW] `main.tsx`: Entry point
- [NEW] `index.css`: Global styles (Tailwind or plain CSS as per standard)

## Verification Plan
### Automated Tests
- Build verification (`npm run build`)
- Lint checks (`npm run lint`)

### Manual Verification
1.  **Start App**: Run `npm run dev`.
2.  **Upload**: Upload a valid Spine export ZIP (json + atlas + png).
3.  **Preview**: Verify the character appears.
4.  **Interact**:
    -   Change animations.
    -   Test playback (pause/play/restart).
    -   Test zoom/pan.
    -   Change background.
