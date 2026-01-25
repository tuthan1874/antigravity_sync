# Add Footer with Social Links and Contact Info

## Goal
Add a comprehensive footer to the landing page with social media links (Facebook, LinkedIn, Behance, ArtStation) and contact information (Website, Email), matching the requested design and functionality.

## Proposed Changes

### [NEW] [Footer.tsx](file:///e:/TDC_App/TD_Games_Studio_App/td-game-studio-hub/src/components/Footer.tsx)
- Create a new `Footer` component.
- Implement variable layout:
    - Row of social icons (Facebook, LinkedIn, Behance, ArtStation).
    - Links should open in new tab (`target="_blank"`).
    - Email address: `info@tdgamestudio.com` (red/highlighted color) and Website link `https://tdgamestudio.com/`.
    - Copyright text.
- Use `lucide-react` for available icons (Facebook, LinkedIn).
- Use inline SVGs for Behance and ArtStation if not available in `lucide-react`.

### [MODIFY] [Index.tsx](file:///e:/TDC_App/TD_Games_Studio_App/td-game-studio-hub/src/pages/Index.tsx)
- Import `Footer` component.
- Replace existing inline footer with `<Footer />`.

## Verification Plan
### Automated Tests
- None.

### Manual Verification
- Open the page in browser.
- Verify all icons are present.
- Verify links hover states and correct URLs.
- Verify layout matches the reference (icons row, email below).
