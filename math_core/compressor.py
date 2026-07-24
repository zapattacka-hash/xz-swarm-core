import numpy as np
import zlib

class StateCompressor:
    @staticmethod
    def compress_quaternion_array(q_array: np.ndarray) -> bytes:
        raw_bytes = q_array.astype(np.float32).tobytes()
        return zlib.compress(raw_bytes)

    @staticmethod
    def decompress_quaternion_array(compressed: bytes, count: int) -> np.ndarray:
        raw = zlib.decompress(compressed)
        return np.frombuffer(raw, dtype=np.float32).reshape((count, 4))

if __name__ == "__main__":
    data = np.array([[1.0, 0.0, 0.0, 0.0], [0.707, 0.707, 0.0, 0.0]])
    comp = StateCompressor.compress_quaternion_array(data)
    decomp = StateCompressor.decompress_quaternion_array(comp, count=2)
    print(f"Original Bytes : {len(data.tobytes())} | Compressed Bytes: {len(comp)}")
