import numpy as np

def hopf_fibration_project(q: np.ndarray) -> np.ndarray:
    """Projects S^3 unit quaternion (q0, q1, q2, q3) to S^2 base sphere (x, y, z)."""
    q0, q1, q2, q3 = q
    x = 2 * (q1*q3 + q0*q2)
    y = 2 * (q2*q3 - q0*q1)
    z = q0**2 + q3**2 - q1**2 - q2**2
    return np.array([x, y, z])

if __name__ == "__main__":
    q = np.array([1.0, 0.0, 0.0, 0.0])
    s2 = hopf_fibration_project(q)
    print(f"S^3 -> S^2 Projection: {s2} | Norm: {np.linalg.norm(s2):.4f}")
