import numpy as np

class CliffordRotor:
    def __init__(self, angle: float, bivector: np.ndarray):
        b_norm = bivector / np.linalg.norm(bivector)
        self.scalar = np.cos(angle / 2.0)
        self.bivector = np.sin(angle / 2.0) * b_norm

    def rotate_vector(self, v: np.ndarray) -> np.ndarray:
        # v' = R v R^\dagger
        return v * (self.scalar**2 - np.dot(self.bivector, self.bivector))

if __name__ == "__main__":
    rotor = CliffordRotor(np.pi / 4, np.array([0.0, 0.0, 1.0]))
    v_rot = rotor.rotate_vector(np.array([1.0, 0.0, 0.0]))
    print(f"Clifford Rotor Transformed Vector: {v_rot}")
