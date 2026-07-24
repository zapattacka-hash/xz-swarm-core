import random

class ChaosMonkey:
    def __init__(self, drop_rate: float = 0.1):
        self.drop_rate = drop_rate

    def should_drop_packet(self) -> bool:
        return random.random() < self.drop_rate

if __name__ == "__main__":
    chaos = ChaosMonkey(drop_rate=0.5)
    print("Simulated Packet Dropped:", chaos.should_drop_packet())
