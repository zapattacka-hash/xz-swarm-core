import numpy as np

def lorentz_spinor_boost(spinor: np.ndarray, beta: float) -> np.ndarray:
    """Applies SL(2, C) Lorentz boost along z-axis with rapidity phi."""
    rapidity = np.arctanh(beta)
    boost_matrix = np.array([
        [np.exp(rapidity/2), 0],
        [0, np.exp(-rapidity/2)]
    ])
    return boost_matrix @ spinor

if __name__ == "__main__":
    sp = np.array([1.0, 0.0])
    boosted = lorentz_spinor_boost(sp, beta=0.5)
    print(f"Boosted Spinor Vector: {boosted}")
