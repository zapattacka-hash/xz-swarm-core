import numpy as np

# Pauli Matrices
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)

def compute_spin_hamiltonian(field_vector: np.ndarray) -> np.ndarray:
    """
    Constructs the 2x2 Spin Hamiltonian H = 0.5 * (Bx*sigma_x + By*sigma_y + Bz*sigma_z).
    field_vector: 3D array [Bx, By, Bz]
    """
    Bx, By, Bz = field_vector
    return 0.5 * (Bx * SIGMA_X + By * SIGMA_Y + Bz * SIGMA_Z)

def evolve_spinor_state(spinor: np.ndarray, field_vector: np.ndarray, dt: float) -> np.ndarray:
    """
    Evolves an SU(2) unit quaternion spinor over time interval dt using Hamiltonian spin dynamics.
    """
    b_norm = np.linalg.norm(field_vector)
    if b_norm < 1e-9:
        return spinor  # No evolution under zero field
    
    b_hat = field_vector / b_norm
    half_angle = 0.5 * b_norm * dt
    
    # Quaternion derivative multiplier (w, x, y, z)
    dq = np.array([
        np.cos(half_angle),
        -b_hat[0] * np.sin(half_angle),
        -b_hat[1] * np.sin(half_angle),
        -b_hat[2] * np.sin(half_angle)
    ])
    
    # Quaternion multiplication (spinor * dq)
    w1, x1, y1, z1 = spinor
    w2, x2, y2, z2 = dq
    
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 - x1*z2 + y1*w2 + z1*x2
    z = w1*z2 + x1*y2 - y1*x2 + z1*w2
    
    evolved = np.array([w, x, y, z])
    return evolved / np.linalg.norm(evolved)

if __name__ == "__main__":
    print("--- Continuous Spin Hamiltonian Phase Engine ---")
    initial_spinor = np.array([1.0, 0.0, 0.0, 0.0])
    field = np.array([0.0, 1.0, 0.0])  # Rotation field around Y-axis
    
    state_t1 = evolve_spinor_state(initial_spinor, field, dt=0.5)
    print(f"Initial State : {initial_spinor}")
    print(f"Evolved State : {state_t1}")
    print(f"Norm Check    : {np.linalg.norm(state_t1):.4f}")
