import numpy as np

class LieAlgebraSU2:
    def __init__(self):
        self.J_x = 0.5 * np.array([[0, 1], [1, 0]], dtype=complex)
        self.J_y = 0.5 * np.array([[0, -1j], [1j, 0]], dtype=complex)
        self.J_z = 0.5 * np.array([[1, 0], [0, -1]], dtype=complex)

    def exp_map(self, theta: float, axis: np.ndarray) -> np.ndarray:
        axis = axis / np.linalg.norm(axis)
        J_vec = axis[0]*self.J_x + axis[1]*self.J_y + axis[2]*self.J_z
        return np.cos(theta/2) * np.eye(2) - 2j * np.sin(theta/2) * J_vec

if __name__ == "__main__":
    su2 = LieAlgebraSU2()
    U = su2.exp_map(np.pi/2, np.array([0, 0, 1]))
    print(f"Lie Exp Map Matrix:\n{U}")
