import struct
import numpy as np

def export_to_wasm_struct(q: np.ndarray) -> bytes:
    """Packs quaternion array into standard 16-byte IEEE 754 float32 binary buffer."""
    return struct.pack("4f", *q.astype(np.float32))

if __name__ == "__main__":
    q = np.array([1.0, 0.0, 0.0, 0.0])
    buf = export_to_wasm_struct(q)
    print(f"WASM Buffer Size: {len(buf)} bytes | Hex: {buf.hex()}")
