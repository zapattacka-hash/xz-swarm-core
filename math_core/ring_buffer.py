import numpy as np

class StateRingBuffer:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.buffer = np.zeros((capacity, 4), dtype=float)
        self.index = 0
        self.size = 0

    def push(self, state: np.ndarray):
        self.buffer[self.index] = state
        self.index = (self.index + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def get_history(() -> np.ndarray:
        return self.buffer[:self.size]

if __name__ == "__main__":
    rb = StateRingBuffer(capacity=5)
    rb.push(np.array([1.0, 0.0, 0.0, 0.0]))
    print(f"Ring Buffer Elements Pushed: {rb.size}")
