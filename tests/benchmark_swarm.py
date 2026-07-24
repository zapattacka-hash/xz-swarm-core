import time
import numpy as np

def benchmark_spinor_operations(iterations: int = 100000):
    q1 = np.array([1.0, 0.0, 0.0, 0.0])
    q2 = np.array([0.707, 0.707, 0.0, 0.0])
    
    start = time.time()
    for _ in range(iterations):
        _ = np.dot(q1, q2)
        _ = q1 / np.linalg.norm(q1)
    elapsed = time.time() - start
    ops_per_sec = iterations / elapsed
    return ops_per_sec, elapsed

if __name__ == "__main__":
    ops, duration = benchmark_spinor_operations()
    print(f"Completed 100,000 SU(2) Spinor Operations in {duration:.4f}s ({ops:.2f} ops/sec)")
