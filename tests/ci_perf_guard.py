import time
import numpy as np

def assert_minimum_performance(min_ops_per_sec: float = 50000.0):
    q = np.array([1.0, 0.0, 0.0, 0.0])
    start = time.time()
    count = 10000
    for _ in range(count):
        _ = q / np.linalg.norm(q)
    elapsed = time.time() - start
    ops = count / elapsed
    assert ops >= min_ops_per_sec, f"Performance regression! {ops:.2f} < {min_ops_per_sec}"
    return ops

if __name__ == "__main__":
    ops = assert_minimum_performance()
    print(f"CI Performance Assert Cleared: {ops:.2f} ops/sec")
