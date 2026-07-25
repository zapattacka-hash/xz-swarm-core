import numpy as np

def Haar_wavelet_decompose(signal: np.ndarray) -> tuple:
    """Simple 1D Haar wavelet transform returning (approx, detail)."""
    approx = (signal[0::2] + signal[1::2]) / np.sqrt(2)
    detail = (signal[0::2] - signal[1::2]) / np.sqrt(2)
    return approx, detail

if __name__ == "__main__":
    sig = np.array([1.0, 2.0, 3.0, 4.0])
    a, d = Haar_wavelet_decompose(sig)
    print(f"Wavelet Approx: {a} | Detail: {d}")
