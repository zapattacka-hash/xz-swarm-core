class BandwidthShaper:
    def __init__(self, max_kbps: float = 1000.0):
        self.max_kbps = max_kbps

    def calculate_delay(self, payload_bytes: int) -> float:
        bits = payload_bytes * 8
        return bits / (self.max_kbps * 1000.0)

if __name__ == "__main__":
    shaper = BandwidthShaper(max_kbps=500.0)
    print(f"Shaped Delay for 1KB Payload: {shaper.calculate_delay(1024):.6f}s")
