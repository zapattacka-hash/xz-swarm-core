import numpy as np

def add_spinor_gaussian_noise(q: np.ndarray, std_dev: float = 0.05) -> np.ndarray:
    """Injects Gaussian noise onto S^3 unit quaternion and re-normalizes."""
    noise = np.random.normal(0, std_dev, size=4)
    perturbed = q + noise
    return perturbed / np.linalg.norm(perturbed)

if __name__ == "__main__":
    q0 = np.array([1.0, 0.0, 0.0, 0.0])
    q_noisy = add_spinor_gaussian_noise(q0)
    print(f"Noisy State: {q_noisy} | Norm: {np.linalg.norm(q_noisy):.4f}")
