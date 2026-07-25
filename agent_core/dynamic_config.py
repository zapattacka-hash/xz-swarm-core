import json

class DynamicConfigEngine:
    def __init__(self):
        self.config = {"tick_rate": 0.05, "byzantine_threshold": 0.4}

    def update_config(self, json_payload: str):
        updates = json.loads(json_payload)
        self.config.update(updates)

if __name__ == "__main__":
    cfg = DynamicConfigEngine()
    cfg.update_config('{"tick_rate": 0.01}')
    print("Updated Config:", cfg.config)
