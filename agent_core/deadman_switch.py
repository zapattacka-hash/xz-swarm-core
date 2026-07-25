import time

class DeadManSwitch:
    def __init__(self, timeout_seconds: float = 5.0):
        self.timeout = timeout_seconds
        self.last_heartbeat = time.time()

    def heartbeat(self):
        self.last_heartbeat = time.time()

    def is_triggered(self) -> bool:
        return (time.time() - self.last_heartbeat) > self.timeout

if __name__ == "__main__":
    dms = DeadManSwitch(timeout_seconds=2.0)
    print(f"Dead-Man Triggered Check: {dms.is_triggered()}")
