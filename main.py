import random
import time
from fusion_engine import MultiModalFusionEngine

class EdgeGuardianEngine:
    def __init__(self):
        self.fusion = MultiModalFusionEngine()
        print("[EdgeGuardian AI] Prototype demo mode")

    def read_demo_telemetry(self):
        return {
            "magnitude": round(random.uniform(0.8, 3.5), 2),
            "vibration": random.choice([0, 1])
        }

    def run(self):
        print("Starting simulated monitoring loop...\n")
        for i in range(1, 6):
            telemetry = self.read_demo_telemetry()
            vision_conf = round(random.uniform(0.4, 0.98), 2)
            state, confidence = self.fusion.evaluate_state(telemetry, vision_conf)

            print(
                f"Sample {i} | Accel Mag: {telemetry['magnitude']}g | "
                f"Vibration: {telemetry['vibration']} | "
                f"Vision Conf: {vision_conf} | "
                f"Status: {state} | Fusion Confidence: {confidence}"
            )
            time.sleep(1)

if __name__ == "__main__":
    EdgeGuardianEngine().run()
