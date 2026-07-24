import numpy as np

def compute_dynamic_field(t: float, base_field: np.ndarray, frequency: float = 1.0) -> np.ndarray:
    """Modulates a 3D potential field over time using harmonic oscillator potentials."""
    modulation = np.array([
        np.sin(frequency * t),
        np.cos(frequency * t),
        np.sin(2 * frequency * t)
    ])
    return base_field * (1.0 + 0.2 * modulation)

if __name__ == "__main__":
    b0 = np.array([0.0, 1.0, 0.0])
    b_t = compute_dynamic_field(t=1.5, base_field=b0)
    print(f"Modulated Field Vector at t=1.5s: {b_t}")
