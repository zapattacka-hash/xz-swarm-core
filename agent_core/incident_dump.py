import json
import time

def generate_incident_dump(node_id: str, reason: str, state: list) -> str:
    return json.dumps({
        "timestamp": time.time(),
        "node_id": node_id,
        "reason": reason,
        "state_snapshot": state
    })

if __name__ == "__main__":
    print("Incident Dump:", generate_incident_dump("node-9", "BYZANTINE_ISOLATION", [0.0, 1.0, 0.0, 0.0]))
