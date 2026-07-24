import hashlib
import time

class AuditLogger:
    def __init__(self):
        self.prev_hash = "0" * 64

    def log_event(self, event_type: str, details: str) -> str:
        timestamp = str(time.time())
        raw = f"{self.prev_hash}|{timestamp}|{event_type}|{details}"
        self.prev_hash = hashlib.sha256(raw.encode('utf-8')).hexdigest()
        return self.prev_hash

if __name__ == "__main__":
    al = AuditLogger()
    h1 = al.log_event("NODE_JOIN", "node-alpha joined cluster")
    print(f"Audit Chain Hash 1: {h1}")
