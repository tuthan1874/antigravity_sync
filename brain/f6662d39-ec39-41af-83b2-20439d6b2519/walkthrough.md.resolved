# VFX Preview Tool — Walkthrough

## What Was Built

A local web-based VFX browser at `f:\Source_Taobao\VFX\tools\` that indexes and previews all **86 VFX effects** (35 Spine + 51 Sprite Sequences).

### Files Created

| File | Purpose |
|------|---------|
| [build-index.js](file:///f:/Source_Taobao/VFX/tools/build-index.js) | Scans VFX folders → generates `vfx-index.json` |
| [server.js](file:///f:/Source_Taobao/VFX/tools/server.js) | Static HTTP server on port 3456 |
| [index.html](file:///f:/Source_Taobao/VFX/tools/index.html) | Preview app with gallery, search, hover preview, animation player |

## How to Use

```bash
cd f:\Source_Taobao\VFX
node tools/build-index.js     # Generate index
node tools/server.js           # Start server → http://localhost:3456
```

## Features

### Gallery with Hover Preview
Hover over any card to see the animation play directly on the thumbnail — no need to click.

![Gallery View](C:\Users\dangt\.gemini\antigravity\brain\f6662d39-ec39-41af-83b2-20439d6b2519\vfx_gallery_view_1774073977182.png)

### Modal Preview with Phase Tabs + 24 FPS Default

````carousel
![Preview Modal](C:\Users\dangt\.gemini\antigravity\brain\f6662d39-ec39-41af-83b2-20439d6b2519\vfx_preview_modal_1774074025269.png)
<!-- slide -->
![Hit Phase](C:\Users\dangt\.gemini\antigravity\brain\f6662d39-ec39-41af-83b2-20439d6b2519\vfx_hit_phase_preview_1774074043103.png)
````

### Demo Recordings

````carousel
![Initial build](C:\Users\dangt\.gemini\antigravity\brain\f6662d39-ec39-41af-83b2-20439d6b2519\vfx_preview_test_1774073962773.webp)
<!-- slide -->
![Hover preview update](C:\Users\dangt\.gemini\antigravity\brain\f6662d39-ec39-41af-83b2-20439d6b2519\hover_preview_test_1774074389455.webp)
````

### Controls
- **Hover** — animation plays directly on gallery card thumbnails
- **Search** — real-time text filter by name/path
- **Type filter** — Tất cả / Spine / Sprite
- **Animation** — ▶ Play/Pause, ⏮⏭ Step, slider scrub, FPS (default 24)
- **Phase tabs** — switch cast1/cast2/hit sub-animations
- **Keyboard** — Space=play, ←→=step, Esc=close
