import numpy as np

def predict_next_spinor(current_state: np.ndarray, velocity: np.ndarray, dt: float = 0.01) -> np.ndarray:
    predicted = current_state + velocity * dt
    return predicted / np.linalg.norm(predicted)

if __name__ == "__main__":
    q0 = np.array([1.0, 0.0, 0.0, 0.0])
    v = np.array([0.0, 0.1, 0.0, 0.0])
    pred = predict_next_spinor(q0, v)
    print(f"Predicted Spinor State: {pred} | Norm: {np.linalg.norm(pred):.4f}")
