# Implementation Plan - Portfolio Animation Spine

## Goal Description
Build a professional portfolio website to showcase Spine animations. The app will allow users to organize animations by Project and Character, upload characters via ZIP files, and view animations directly in the browser.

## User Review Required
> [!IMPORTANT]
> **Storage Constraint**: The user explicitly requested `window.storage` and NO `localStorage`. I will implement a custom `StorageAPI` backed by **IndexedDB** (to handle large ZIP/Image blobs) and expose it globally or via a React Context, adhering to the "persistent" requirement.

> [!WARNING]
> **Spine Assets**: The user specified the ZIP contains a `.spine` file and `images/` folder, but NO `.atlas` file. Standard Spine runtimes usually require an atlas.
> **Strategy**: I will assume the `.spine` file is the Skeleton JSON export. I will implement a mechanism to dynamically serve the images from the ZIP blobs to the Spine runtime, effectively bypassing the standard Atlas requirement if possible, or generating a virtual atlas in-memory.

## Proposed Changes

### Infrastructure
#### [NEW] [storage.ts](file:///src/lib/storage.ts)
- Implementation of the persistent storage using `idb` (IndexedDB wrapper).
- Methods: `saveProject`, `getProjects`, `saveCharacter`, `getCharacters`, `deleteCharacter`, etc.
- Handles storing large Blobs (images/skeleton data).

#### [NEW] [spine-loader.ts](file:///src/lib/spine-loader.ts)
- Utilities to parse ZIP files using `jszip`.
- Validation logic (check for `.spine`, `images/`, `avatar.png`).
- Helper to create Blob URLs for the Spine Player.

### Components

#### [NEW] [App.tsx](file:///src/App.tsx)
- Main layout with Sidebar (Projects) and Main Content (Grid/Viewer).

#### [NEW] [ProjectSidebar.tsx](file:///src/components/ProjectSidebar.tsx)
- List of projects.
- Add/Delete project functionality.

#### [NEW] [CharacterGrid.tsx](file:///src/components/CharacterGrid.tsx)
- Grid display of characters for the selected project.
- Thumbnail display (avatar.png).
- Upload button/zone.

#### [NEW] [SpineViewer.tsx](file:///src/components/SpineViewer.tsx)
- Wrapper around `@esotericsoftware/spine-player`.
- Handles mounting/unmounting of the player.
- Controls for animation switching, speed, pause/play.

#### [NEW] [UploadModal.tsx](file:///src/components/UploadModal.tsx)
- Drag and drop zone.
- Progress bar for ZIP processing.

## Verification Plan

### Automated Tests
- N/A (Focus on manual verification for UI/Animation).

### Manual Verification
1.  **Project Management**: Create, Rename, Delete projects. Verify persistence after reload.
2.  **Upload Flow**: Upload a valid ZIP. Verify parsing and thumbnail display. Upload invalid ZIP, verify error message.
3.  **Animation**: Click a character. Verify Spine player loads. Check if animations play, loop, and switch correctly.
4.  **Persistence**: Reload page. Ensure Projects and Characters (and their images) are still loaded from IndexedDB.
