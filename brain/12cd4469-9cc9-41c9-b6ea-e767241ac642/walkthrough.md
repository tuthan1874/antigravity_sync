# Walkthrough - TDGames_App Backend Deployment

I have successfully deployed the backend for **TDGames_App** on Supabase.

## Project Details
- **Project Name**: `TDGames_App`
- **Organization**: `TDGames_App`
- **Region**: `ap-southeast-1`
- **Project ID**: `ldckhfaulfjtxiznrzib`
- **Status**: `ACTIVE_HEALTHY`

## Database Schema

I created the following tables with RLS enabled:

### `projects`
- Stores project metadata.
- **RLS**: Public Read, Admin (Authenticated) Full Access.

### `files`
- Stores references to PSD/Spine files and metadata.
- **RLS**: Public Read, Admin (Authenticated) Full Access.

### `feedback`
- Stores user comments, drawings, and screenshots.
- **RLS**: Public Read/Insert, Admin Delete.
- **Guest Access**: Enabled via Public Insert policy.

## Storage Buckets

Two public buckets were created:
1.  **`project_assets`**: For admin-uploaded PSD/Spine files.
    - Public Read.
    - Authenticated Write/Delete.
2.  **`feedback_assets`**: For user-uploaded screenshots.
    - Public Read.
    - Public Write (for guests).

## Next Steps
- Connect your frontend application using the Project ID `ldckhfaulfjtxiznrzib`.
- Use the `anon` key for public/guest access and `service_role` (backend only) or Auth for admin access.
