import numpy as np

def symplectic_euler_step(q: np.ndarray, p: np.ndarray, dt: float = 0.01) -> tuple:
    """Energy-preserving symplectic step for phase space (q, p)."""
    p_next = p - dt * q  # Harmonic oscillator potential dV/dq = q
    q_next = q + dt * p_next
    return q_next, p_next

if __name__ == "__main__":
    q0, p0 = np.array([1.0, 0.0]), np.array([0.0, 1.0])
    q1, p1 = symplectic_euler_step(q0, p0)
    print(f"Symplectic Phase Step: q={q1}, p={p1}")
