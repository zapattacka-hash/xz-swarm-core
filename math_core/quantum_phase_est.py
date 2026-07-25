import numpy as np

def estimate_quantum_phase(eigenvalue: complex) -> float:
    """Extracts phase theta from complex eigenvalue e^(2pi * i * theta)."""
    phase = np.angle(eigenvalue) / (2.0 * np.pi)
    return float(phase if phase >= 0 else phase + 1.0)

if __name__ == "__main__":
    ev = np.exp(2j * np.pi * 0.25)
    print(f"Estimated Phase: {estimate_quantum_phase(ev):.4f}")
