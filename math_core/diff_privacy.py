import numpy as np

def apply_differential_privacy(q: np.ndarray, epsilon: float = 1.0) -> np.ndarray:
    """Applies Laplacian noise to unit quaternion for privacy preservation."""
    beta = 1.0 / epsilon
    noise = np.random.laplace(0, beta, size=4)
    masked = q + noise
    return masked / np.linalg.norm(masked)

if __name__ == "__main__":
    q0 = np.array([1.0, 0.0, 0.0, 0.0])
    dp_q = apply_differential_privacy(q0)
    print(f"Privacy Masked State: {dp_q} | Norm: {np.linalg.norm(dp_q):.4f}")
