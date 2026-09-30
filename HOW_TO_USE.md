# How to use this ZIP

1. Extract the ZIP.
2. Open a terminal in `EdgeGuardian-AI`.
3. Run:
   `python src/main.py`
4. For ESP32 hardware, upload:
   `firmware/esp32_telemetry/esp32_telemetry.ino`
5. Set your actual COM port in `config/system_config.json`.
6. Next development step: add a Python serial reader and connect it to `MultiModalFusionEngine`.

The file `docs/original_submitted_generator.py` is the source you originally uploaded.
