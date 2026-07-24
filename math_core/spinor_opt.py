import numpy as np

def optimize_spinor_step(q1: np.ndarray, q2: np.ndarray, t: float) -> np.ndarray:
    """
    Computes the optimized geodesic path step (SLERP) between two unit 
    spinors represented as quaternions, respecting SU(2) double-cover geometry.
    """
    q1 = q1 / np.linalg.norm(q1)
    q2 = q2 / np.linalg.norm(q2)
    
    dot = np.dot(q1, q2)
    
    # Invert sign if dot product is negative to preserve shortest double-cover path
    if dot < 0.0:
        q2 = -q2
        dot = -dot
        
    DOT_THRESHOLD = 0.9995
    if dot > DOT_THRESHOLD:
        result = q1 + t * (q2 - q1)
        return result / np.linalg.norm(result)
    
    theta_0 = np.arccos(dot)
    theta_t = theta_0 * t
    sin_theta_0 = np.sin(theta_0)
    sin_theta_t = np.sin(theta_t)
    
    s0 = np.sin(theta_0 - theta_t) / sin_theta_0
    s1 = sin_theta_t / sin_theta_0
    
    return (s0 * q1) + (s1 * q2)

if __name__ == "__main__":
    initial_spinor = np.array([1.0, 0.0, 0.0, 0.0])
    target_spinor = np.array([-0.707, 0.0, 0.707, 0.0])
    
    optimized_midpoint = optimize_spinor_step(initial_spinor, target_spinor, 0.5)
    print("--- Spinor Geodesic Optimization ---")
    print(f"Optimized Midpoint Quaternion State: {optimized_midpoint}")
