# Plan: Update UI Color Scheme and Logo

Change the primary color from orange to pink (#de0a67) and update the overall theme to be pink/white. Replace the header logo with the new TD CONSULTING logo.

## Proposed Changes

### Styling

#### [MODIFY] [index.css](file:///e:/TDC_App/TD_Consulting_App/hiring_tdconsulting/src/index.css)

Update CSS variables in `:root` and `.dark` to use pink (#de0a67) as the primary color:
- `--primary`: Change from `35 100% 50%` (orange) to `336 92% 45%` (pink #de0a67)
- `--accent`: Change to match the new primary color
- `--border`: Update to use new primary color
- `--ring`: Update to use new primary color
- Update `pulse-glow` animation to use pink color

---

### Logo

#### [DELETE] [tdgames-logo.png](file:///e:/TDC_App/TD_Consulting_App/hiring_tdconsulting/src/assets/tdgames-logo.png)

Remove the old TD GAMES logo.

#### [NEW] [tdconsulting-logo.png](file:///e:/TDC_App/TD_Consulting_App/hiring_tdconsulting/src/assets/tdconsulting-logo.png)

Add the new TD CONSULTING logo from the uploaded image.

#### [MODIFY] [Index.tsx](file:///e:/TDC_App/TD_Consulting_App/hiring_tdconsulting/src/pages/Index.tsx)

- Update the import statement to use the new logo file
- Update the `alt` text and `drop-shadow` style to use pink color

---

### SEO/Meta Updates

#### [MODIFY] [Index.tsx](file:///e:/TDC_App/TD_Consulting_App/hiring_tdconsulting/src/pages/Index.tsx)

Update page title and meta description to reference TD CONSULTING instead of TD GAMES.

## Verification Plan

### Manual Verification
- View the application at http://localhost:8080
- Verify the new pink color scheme is applied throughout
- Verify the new logo is displayed correctly in the header
