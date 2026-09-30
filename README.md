# EdgeGuardian AI — Driver Safety Prototype

## What this project is

EdgeGuardian AI is a prototype concept for a driver-safety assistant. The intended system combines:

- ESP32 telemetry
- MPU6050 acceleration/gyro data
- vibration sensing
- GPS telemetry (planned/in the architecture)
- laptop camera computer vision (planned)
- a local Python fusion engine
- optional ONNX/QNN/Qualcomm AI Hub acceleration (planned)

The intended output is one of four states:

`NORMAL` → `RISK DETECTED` → `POSSIBLE ACCIDENT` → `EMERGENCY`

## Current implementation status

### Working in the supplied code
- ESP32 reads MPU6050 data.
- Acceleration magnitude is converted to approximately `g`.
- A digital vibration input is read.
- Telemetry is emitted as JSON over USB serial.
- A Python fusion engine contains threshold-based classification logic.
- A demo `main.py` runs without hardware by generating random sample telemetry.

### Not actually implemented yet
- Real laptop-camera driver-state detection.
- Real eye/head-pose/distraction model.
- GPS parsing/use in the Python fusion engine.
- Actual ONNX model file (`models/driver_state_quant.onnx`).
- Verified Qualcomm QNN execution.
- Real-time dashboard/UI.
- Automated emergency SMS/call.
- Production-grade accident detection.

## Hardware prototype

Suggested hardware based on the supplied firmware:
- ESP32
- MPU6050
- Digital vibration sensor
- Optional GPS module

The ESP32 firmware uses I2C for the MPU6050 and USB serial at 115200 baud.

## Run the software demo

From this directory:

```bash
python src/main.py
```

The demo currently uses simulated/random telemetry, so no ESP32 is required for this mode.

## Run with ESP32 telemetry

The supplied firmware prints JSON such as:

```json
{"magnitude":1.023,"vibration":0}
```

You would then need to add a Python serial reader (for example with `pyserial`) that reads the COM port and passes the JSON into `MultiModalFusionEngine.evaluate_state()`.

## Suggested development order

1. Connect ESP32 + MPU6050 and verify serial telemetry.
2. Add a Python serial reader.
3. Calibrate acceleration/impact thresholds using recorded real data.
4. Add camera capture with OpenCV.
5. Add a real driver-state/attention model.
6. Fuse sensor and vision confidence rather than using only fixed thresholds.
7. Add a local dashboard and event log.
8. Only then benchmark/optimize an actual ONNX model for the target Snapdragon device.

## Important presentation note

This repository should be presented as a **prototype / proof of concept**. Do not claim that camera AI, Qualcomm NPU inference, GPS integration, or emergency automation is already working unless those components have actually been implemented and tested.
