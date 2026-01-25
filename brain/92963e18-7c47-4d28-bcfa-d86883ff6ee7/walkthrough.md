# Simplified ClickUp Clone Walkthrough

I have successfully created a simplified ClickUp clone using React, Tailwind CSS, and Firebase.

## Features Implemented

### 1. Project Structure
- **Single File Logic**: All application logic resides in `src/App.tsx` for simplicity.
- **Tailwind CSS v4**: Configured for modern, high-performance styling.
- **Firebase Integration**: Ready for real-time data sync (requires configuration).

### 2. User Interface
- **Sidebar**: Navigation for "Spaces" (Projects) with active state styling.
- **Task Views**:
    - **List View**: Table-like list of tasks.
    - **Board View**: Kanban-style columns (Todo, In Progress, Done).
- **Dark Mode Aesthetics**: sleek, dark-themed UI inspired by ClickUp.

### 3. Task Management
- **Create Task**: Modal to add new tasks with title and priority.
- **Status Updates**: Click status badges to cycle through Todo -> In Progress -> Done.
- **Delete**: Remove tasks (hover action).
- **Real-time Sync**: Automatically syncs with Firestore if configured; falls back to local state if not.

## How to Run

1.  **Install Dependencies** (if not already done):
    ```bash
    npm install
    ```
2.  **Start Development Server**:
    ```bash
    npm run dev
    ```
3.  **Build for Production**:
    ```bash
    npm run build
    ```

## Firebase Configuration
To enable real-time features, update the `firebaseConfig` object in `src/App.tsx` with your project details:

```typescript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  // ... other config
};
```

## Verification Results
- [x] **Build**: `npm run build` passed successfully.
- [x] **UI**: Verified dark mode styling and layout structure.
- [x] **Logic**: Verified fallback to mock data when Firebase is not configured.
