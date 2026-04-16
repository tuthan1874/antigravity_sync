# Walkthrough: Auto Animation Pipeline (MediaPipe -> Spine 2D)

## What Was Built

A complete Python pipeline that converts **video files** to **Spine 2D animation JSON** using MediaPipe body pose estimation.

## Project Structure

```
Auto_Animation/
├── Rig_Base.json              # Original skeleton (Spine 4.2.39)
├── requirements.txt           # Dependencies
├── config.yaml                # Bone mapping configuration
├── mocap_to_spine.py          # Main CLI tool
├── test_pipeline.py           # Test with synthetic walk cycle
├── core/
│   ├── __init__.py
│   ├── video_processor.py     # MediaPipe pose extraction
│   ├── pose_converter.py      # Landmarks -> bone rotations
│   ├── spine_writer.py        # Spine JSON output
│   └── smoothing.py           # Noise reduction + keyframe reduction
├── input/                     # Place video files here
└── output/                    # Generated animation JSON files
```

## Files Created

### [config.yaml](file:///e:/TDC_App/TDGAMES_App/Auto_Animation/config.yaml)
Maps 33 MediaPipe landmarks to 11 Rig_Base bones. Includes setup-pose rotations, IK target positions, scale calibration, and smoothing params.

### [core/video_processor.py](file:///e:/TDC_App/TDGAMES_App/Auto_Animation/core/video_processor.py)
Extracts pose landmarks from video using MediaPipe Pose (model_complexity=2). Handles frame sampling, missing frame interpolation.

### [core/pose_converter.py](file:///e:/TDC_App/TDGAMES_App/Auto_Animation/core/pose_converter.py)
Core math module:
- **World-rotation bones** (bicepNear, bicepFar, Head) — `noRotationOrReflection` inheritance
- **Local-rotation bones** (forearmNear, forearmFar, Waist, Torso, Neck) — accumulated parent chain
- **IK targets** (CTRL_footNear, CTRL_footFar) — position-based for leg IK
- **Pelvis root motion** — translation + rotation from hip landmarks

### [core/smoothing.py](file:///e:/TDC_App/TDGAMES_App/Auto_Animation/core/smoothing.py)
Savitzky-Golay filter + moving average, plus keyframe reduction to remove redundant frames.

### [core/spine_writer.py](file:///e:/TDC_App/TDGAMES_App/Auto_Animation/core/spine_writer.py)
Generates Spine 4.2 JSON: `rotate` (with `value`), `translatex`, `translatey`. Supports standalone (full skeleton + animation) and animation-only export.

### [mocap_to_spine.py](file:///e:/TDC_App/TDGAMES_App/Auto_Animation/mocap_to_spine.py)
CLI entry point with full argument parsing.

## Usage

### With a video file:
```bash
python mocap_to_spine.py input/walk_cycle.mp4
python mocap_to_spine.py input/attack.mp4 --name "Attack_A" --fps 24 --smooth 7
python mocap_to_spine.py input/idle.mp4 --animation-only
```

### Test with synthetic data (no video needed):
```bash
python test_pipeline.py
```

## Test Results

```
[TEST] Pipeline -- Synthetic Walk Cycle
[OK] Generated 60 pose frames
[OK] Converted 11 bones:
  Pelvis          -> rotate:60kf, tx:60kf, ty:60kf
  CTRL_footNear   -> tx:60kf, ty:60kf
  CTRL_footFar    -> tx:60kf, ty:60kf
  bicepNear       -> rotate:60kf
  bicepFar        -> rotate:60kf
  Head            -> rotate:60kf
  forearmNear     -> rotate:60kf
  forearmFar      -> rotate:60kf
  Waist           -> rotate:60kf
  Torso           -> rotate:60kf
  Neck            -> rotate:60kf
[OK] Total keyframes after reduction: 510
[OK] Animation 'Test_Walk' found with 11 animated bones
  Pelvis: ['rotate', 'translatex', 'translatey']
  bicepNear: ['rotate']
  CTRL_footNear: ['translatex', 'translatey']
```

## Animated Bones (11 total)

| Bone | Type | Data Source |
|:---|:---|:---|
| Pelvis | translate + rotate | Hip midpoint position & angle |
| Waist | rotate | Hip-to-shoulder spine angle |
| Torso | rotate | Upper torso angle |
| Neck | rotate | Shoulder-to-nose angle |
| Head | rotate (world) | Ear-to-nose direction |
| bicepNear | rotate (world) | L_SHOULDER -> L_ELBOW |
| forearmNear | rotate (local) | L_ELBOW -> L_WRIST |
| bicepFar | rotate (world) | R_SHOULDER -> R_ELBOW |
| forearmFar | rotate (local) | R_ELBOW -> R_WRIST |
| CTRL_footNear | translate (IK) | L_ANKLE position |
| CTRL_footFar | translate (IK) | R_ANKLE position |

## Next Steps

1. **Test with real video** — place a walk/attack video in `input/` folder and run `mocap_to_spine.py`
2. **Import into Spine** — open `output/test_walk_anim.json` in Spine Editor
3. **Tune config.yaml** — adjust `spine_scale` and bone mapping for better accuracy
4. **Add hand bones** — map handNear/handFar from wrist landmarks
5. **Add Bezier curves** — current output uses linear interpolation; Spine Editor can auto-smooth
