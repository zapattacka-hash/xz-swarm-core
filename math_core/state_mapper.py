import numpy as np

def metrics_to_spinor(cpu_load: float, latency_ms: float, bandwidth_usage: float) -> np.ndarray:
    """
    Maps 3D operational telemetry onto an SU(2) unit spinor.
    """
    theta = cpu_load * np.pi
    phi = bandwidth_usage * 2 * np.pi
    omega = (latency_ms / 1000.0) * np.pi
    
    w = np.cos(theta / 2) * np.cos(omega)
    x = np.sin(theta / 2) * np.cos(phi)
    y = np.sin(theta / 2) * np.sin(phi)
    z = np.cos(theta / 2) * np.sin(omega)
    
    spinor = np.array([w, x, y, z])
    return spinor / np.linalg.norm(spinor)

if __name__ == "__main__":
    test_spinor = metrics_to_spinor(cpu_load=0.45, latency_ms=25.0, bandwidth_usage=0.80)
    print("--- Metric to Spinor Mapping ---")
    print(f"Mapped SU(2) State: {test_spinor}")
    print(f"Norm: {np.linalg.norm(test_spinor):.4f}")
