class EdgeProxy:
    def __init__(self, batch_size: int = 5):
        self.batch_size = batch_size
        self.queue = []

    def push_telemetry(self, item: dict) -> bool:
        self.queue.append(item)
        return len(self.queue) >= self.batch_size

    def flush(self) -> list:
        batch = self.queue[:]
        self.queue.clear()
        return batch

if __name__ == "__main__":
    proxy = EdgeProxy(batch_size=2)
    print("Flushed Ready:", proxy.push_telemetry({"node": "edge-1"}))
    print("Flushed Ready:", proxy.push_telemetry({"node": "edge-2"}))
    print("Flushed Batch:", len(proxy.flush()))
