import numpy as np

def compute_chern_number(berry_flux: float) -> int:
    """Calculates integer Chern invariant from integrated Berry curvature."""
    return int(np.round(berry_flux / (2.0 * np.pi)))

if __name__ == "__main__":
    flux = 2.0 * np.pi * 1.002
    print(f"Topological Chern Number: {compute_chern_number(flux)}")
