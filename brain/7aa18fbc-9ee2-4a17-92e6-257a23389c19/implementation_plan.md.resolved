# MediaPipe → Spine JSON Auto Animation Pipeline

## Goal
Build a Python tool that takes a video file as input, extracts human body pose via MediaPipe, and outputs a Spine 2D animation JSON that can be imported into the existing `Rig_Base.json` skeleton.

## Proposed Structure

### Project Layout
```
Auto_Animation/
├── Rig_Base.json              # Existing skeleton (untouched)
├── requirements.txt           # Dependencies
├── config.yaml                # Bone mapping + calibration config
├── mocap_to_spine.py          # Main CLI entry point
├── core/
│   ├── __init__.py
│   ├── video_processor.py     # MediaPipe pose extraction
│   ├── pose_converter.py      # Convert landmarks → bone rotations
│   ├── spine_writer.py        # Write Spine JSON animation
│   └── smoothing.py           # Signal smoothing (noise reduction)
├── input/                     # Place video files here
└── output/                    # Generated Spine JSON files
```

### Key Components

#### 1. `video_processor.py` — MediaPipe Extraction
- Read video frame-by-frame with OpenCV
- Extract 33 pose landmarks using MediaPipe Pose
- Return structured per-frame landmark data with timestamps

#### 2. `pose_converter.py` — Landmarks → Bone Rotations
- Map MediaPipe landmarks to Rig_Base bones
- Calculate rotation angles from joint vectors
- Handle IK targets: compute CTRL_footNear/CTRL_footFar positions
- Handle coordinate system differences (MediaPipe normalized → Spine world coords)

**Critical bone mapping:**
| Spine Bone | MediaPipe Landmarks | Calculation |
|:---|:---|:---|
| Pelvis (translate) | HIPS midpoint | Position relative to DeathScaler |
| Waist (rotate) | HIP→SHOULDER vector | Angle of spine column |
| Torso (rotate) | SHOULDER line angle | Upper body rotation |
| Neck (rotate) | Shoulder→Nose vector | Neck bend |
| Head (rotate) | Nose + Ear positions | Head tilt |
| bicepNear (rotate) | L_SHOULDER→L_ELBOW | Upper arm angle |
| forearmNear (rotate) | L_ELBOW→L_WRIST | Forearm angle |
| bicepFar (rotate) | R_SHOULDER→R_ELBOW | Upper arm angle |
| forearmFar (rotate) | R_ELBOW→R_WRIST | Forearm angle |
| CTRL_footNear (translate) | L_ANKLE position | IK target for left leg |
| CTRL_footFar (translate) | R_ANKLE position | IK target for right leg |

#### 3. `spine_writer.py` — Animation JSON Generator
- Read existing Rig_Base.json
- Generate animation keyframes in Spine 4.2 format
- Support `rotate`, `translatex`, `translatey` timelines
- Use linear interpolation (Spine Editor can re-curve later)

#### 4. `smoothing.py` — Noise Reduction
- Moving average filter
- Optional Savitzky-Golay filter
- Keyframe reduction (remove redundant frames)

### CLI Usage
```bash
python mocap_to_spine.py input/walk_cycle.mp4 --output output/walk_anim.json --name "Walk" --fps 30 --smooth 5
```

## Verification Plan
1. Run with a simple walk cycle video
2. Import output JSON into Spine Editor
3. Verify bones move correctly with the skeleton

## Open Questions

> [!IMPORTANT]
> The Rig_Base uses a mix of `rotate`+`value` and `translatex`/`translatey` (separate X/Y) in Spine 4.2 format. Both the combined `translate` (with x,y) and separate `translatex`/`translatey` appear in Active_A. I'll support both but default to the separate format since that's what Spine 4.2 prefers.
