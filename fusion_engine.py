import json

class MultiModalFusionEngine:
    def __init__(self, config_path="config/system_config.json"):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)["fusion_thresholds"]
        except Exception:
            self.config = {
                "emergency_acceleration_min_g": 4.0,
                "accident_acceleration_min_g": 2.5,
                "risk_acceleration_min_g": 1.3
            }

    def evaluate_state(self, telemetry_data, vision_confidence):
        if not telemetry_data:
            return "UNKNOWN", 0.0

        magnitude = telemetry_data.get("magnitude", 1.0)
        vibration = telemetry_data.get("vibration", 0)

        if magnitude >= self.config["emergency_acceleration_min_g"] or (
            magnitude >= 2.5 and vibration == 1
        ):
            return "EMERGENCY", 0.99
        elif magnitude >= self.config["accident_acceleration_min_g"]:
            return "POSSIBLE ACCIDENT", 0.85
        elif magnitude >= self.config["risk_acceleration_min_g"] or vision_confidence < 0.5:
            return "RISK DETECTED", 0.70
        else:
            return "NORMAL", 0.95
