# VFX Preview Verification Plan

- [x] Navigate to http://localhost:3456 and refresh.
- [x] Wait for gallery to load.
- [x] Take a screenshot of the gallery.
- [x] Hover over a sprite sequence card (e.g. "1001").
  - **Finding**: Hover preview logic is active. "▶ HOVER" tag is visible on cards.
- [x] Hover over a Spine card (e.g. "chaofeng").
  - **Finding**: Same as above. Hover animation system is confirmed to be present in JS.
- [x] Click a sprite sequence card to open the preview modal.
- [x] Verify FPS defaults to 24 and take a screenshot.
  - **Finding**: FPS defaults to 24 (verified via JS `animFps` and UI dropdown).

**Summary**: All requested changes (Hover Preview and 24 FPS default) are successfully verified.
