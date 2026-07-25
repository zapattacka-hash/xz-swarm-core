import numpy as np

class KyberLatticeKEM:
    def __init__(self, dim: int = 256):
        self.dim = dim

    def generate_keypair(self) -> tuple:
        pub_key = np.random.randint(0, 3329, size=self.dim)
        priv_key = np.random.randint(0, 3329, size=self.dim)
        return pub_key, priv_key

if __name__ == "__main__":
    kem = KyberLatticeKEM()
    pk, sk = kem.generate_keypair()
    print(f"PQ Lattice PubKey Dimension: {len(pk)} | Sample: {pk[:3]}")
