# Full UI/UX Redesign — Orange Theme with Light/Dark Mode

## Goal
Redesign the entire ChatSync dashboard with:
- **Light Theme**: Orange + White — clean, bright, professional
- **Dark Theme**: Orange + Black — premium, modern, high-contrast
- Theme toggle button in sidebar

## Design System (from UI/UX Pro Max Skill)

### Color Palette
| Token | Light Theme | Dark Theme |
|-------|-------------|------------|
| `--primary` | `#EA580C` (deep orange) | `#F97316` (bright orange) |
| `--primary-hover` | `#C2410C` | `#FB923C` |
| `--bg-primary` | `#FAFAF9` (warm white) | `#0C0A09` (warm black) |
| `--bg-secondary` | `#FFFFFF` | `#1C1917` |
| `--bg-card` | `#FFFFFF` | `#292524` |
| `--bg-hover` | `#FFF7ED` (orange tint) | `#44403C` |
| `--bg-input` | `#F5F5F4` | `#1C1917` |
| `--border` | `#E7E5E4` | `#44403C` |
| `--text-primary` | `#0C0A09` | `#FAFAF9` |
| `--text-secondary` | `#57534E` | `#A8A29E` |
| `--text-muted` | `#A8A29E` | `#78716C` |
| `--accent` | `#EA580C` | `#F97316` |
| `--success` | `#16A34A` | `#22C55E` |
| `--warning` | `#D97706` | `#FBBF24` |
| `--error` | `#DC2626` | `#EF4444` |
| `--info` | `#2563EB` | `#3B82F6` |

### Typography (Skill: "Dashboard Data" pairing)
- **Headings**: `Inter` (weight 600-700) — modern, clean
- **Body**: `Inter` (weight 400-500)
- **Data/Monospace**: `Fira Code` — for IDs, URLs, code

### Design Principles
- Clean Flat Design with subtle shadows
- Orange gradient accents for primary actions
- Smooth micro-animations (hover, page transitions)
- Consistent 8px spacing grid
- `border-radius: 12px` for cards, `8px` for buttons/inputs

## Proposed Changes

### CSS — Complete Rewrite

#### [MODIFY] [index.css](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/index.css)

Full rewrite of the design system with:
1. **`:root`** — Light theme variables (default)
2. **`[data-theme="dark"]`** — Dark theme overrides
3. **Sidebar** — Orange accent, logo gradient → orange
4. **Stats grid** — Orange-tinted stat icons
5. **Cards/Tables** — Clean borders, proper contrast
6. **Buttons** — Orange gradient primary, neutral secondary
7. **Badges** — Same semantic colors (success/warning/error)
8. **Modals** — Updated backgrounds
9. **Login** — Orange gradient background
10. **Theme toggle** — Sun/moon icon button in sidebar

### HTML — Add Theme Toggle

#### [MODIFY] [index.html](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/index.html)

- Add theme toggle button in sidebar footer
- Add `<link>` for Google Fonts (Inter + Fira Code)

### JS — Theme Persistence

#### [MODIFY] [app.js](file:///e:/TDC_App/TDGAMES_App/Sync_Slack_Discord_ClickUp_Drive/public/app.js)

- Add `toggleTheme()` function
- Save preference to `localStorage`
- Apply on page load

## Verification Plan
- Start server, open in browser
- Verify Light and Dark themes
- Toggle between themes
- Check all pages: Dashboard, Chat Sync, Drive Sync, PM Tracking, Customers, Projects, List Configs, Sync Logs, Name Mappings, Settings
