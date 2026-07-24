import json

class RedisSyncBroker:
    def __init__(self, channel: str = "xz-swarm-telemetry"):
        self.channel = channel
        self.published_messages = []

    def publish_state(self, agent_id: str, state: list) -> str:
        payload = json.dumps({"agent_id": agent_id, "state": state})
        self.published_messages.append(payload)
        return payload

if __name__ == "__main__":
    broker = RedisSyncBroker()
    msg = broker.publish_state("node-alpha", [1.0, 0.0, 0.0, 0.0])
    print(f"Published to Redis Channel '{broker.channel}': {msg}")
