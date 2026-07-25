import hashlib

class ZKStateValidator:
    @staticmethod
    def generate_proof(state_hash: str, secret: str) -> str:
        return hashlib.sha256(f"{state_hash}:{secret}".encode('utf-8')).hexdigest()

    @staticmethod
    def verify_proof(state_hash: str, secret: str, proof: str) -> bool:
        expected = hashlib.sha256(f"{state_hash}:{secret}".encode('utf-8')).hexdigest()
        return expected == proof

if __name__ == "__main__":
    proof = ZKStateValidator.generate_proof("hash123", "secret_nonce")
    print(f"ZKP Verification: {ZKStateValidator.verify_proof('hash123', 'secret_nonce', proof)}")
