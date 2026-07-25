import numpy as np

def compute_riemannian_distance_matrix(states: list) -> np.ndarray:
    n = len(states)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dot = np.clip(np.abs(np.dot(states[i], states[j])), 0.0, 1.0)
            matrix[i, j] = 2.0 * np.arccos(dot)
    return matrix

if __name__ == "__main__":
    s = [np.array([1.0, 0.0, 0.0, 0.0]), np.array([0.707, 0.707, 0.0, 0.0])]
    print("Riemannian Distance Matrix:\n", compute_riemannian_distance_matrix(s))
