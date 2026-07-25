import numpy as np

class Octonion:
    def __init__(self, vec: np.ndarray):
        self.vec = vec / np.linalg.norm(vec)

    def norm(self) -> float:
        return float(np.linalg.norm(self.vec))

if __name__ == "__main__":
    octo = Octonion(np.ones(8))
    print(f"8D Octonion Norm: {octo.norm():.4f}")
