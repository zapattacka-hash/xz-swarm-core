import numpy as np

class QuaternionKalmanFilter:
    def __init__(self, process_noise: float = 0.01, measure_noise: float = 0.1):
        self.state = np.array([1.0, 0.0, 0.0, 0.0])
        self.p_var = 1.0
        self.q_var = process_noise
        self.r_var = measure_noise

    def update(self, measurement: np.ndarray) -> np.ndarray:
        # Simplified 1D covariance update over unit norm manifold
        k_gain = self.p_var / (self.p_var + self.r_var)
        self.state = (1.0 - k_gain) * self.state + k_gain * measurement
        self.state /= np.linalg.norm(self.state)
        self.p_var = (1.0 - k_gain) * self.p_var + self.q_var
        return self.state

if __name__ == "__main__":
    kf = QuaternionKalmanFilter()
    est = kf.update(np.array([0.9, 0.1, 0.0, 0.0]))
    print(f"Kalman Filtered State: {est} | Norm: {np.linalg.norm(est):.4f}")
