import json

class WebhookDispatcher:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def format_alert_payload(self, alert_type: str, message: str) -> str:
        return json.dumps({
            "target": self.endpoint,
            "alert": alert_type,
            "message": message
        })

if __name# 1. Properly close and save agent_core\webhook_dispatcher.py
@'
import json

class WebhookDispatcher:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def format_alert_payload(self, alert_type: str, message: str) -> str:
        return json.dumps({
            "target": self.endpoint,
            "alert": alert_type,
            "message": message
        })

if __name__ == "__main__":
    disp = WebhookDispatcher("https://hooks.xz-labs.io/alerts")
    print("Alert Payload:", disp.format_alert_payload("BYZANTINE_DETECTED", "node-3 isolated"))
