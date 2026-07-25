import numpy as np

def quaternion_fft(q_signal: np.ndarray) -> np.ndarray:
    """Applies FFT across component channels of hypercomplex spatial signal."""
    fft_components = [np.fft.fft(q_signal[:, i]) for i in range(4)]
    return np.column_stack(fft_components)

if __name__ == "__main__":
    sig = np.random.rand(16, 4)
    q_fft = quaternion_fft(sig)
    print(f"QFFT Output Shape: {q_fft.shape}")
