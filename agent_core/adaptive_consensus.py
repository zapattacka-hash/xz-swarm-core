import numpy as np

def compute_adaptive_rate(mean_drift: float, base_rate: float = 0.1, max_rate: float = 0.5) -> float:
    """Calculates dynamically scaled correction step based on cluster variance/drift."""
    scaled_rate = base_rate * (1.0 + 5.0 * mean_drift)
    return float(np.clip(scaled_rate, base_rate, max_rate))

if __name__ == "__main__":
    rate = compute_adaptive_rate(mean_drift=0.08)
    print(f"Adaptive Consensus Correction Step: {rate:.4f}")
