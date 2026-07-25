import time

class CertRotator:
    def __init__(self, ttl_seconds: float = 3600.0):
        self.ttl = ttl_seconds
        self.issued_at = time.time()

    def is_expired(self) -> bool:
        return (time.time() - self.issued_at) > self.ttl

if __name__ == "__main__":
    rot = CertRotator(ttl_seconds=10.0)
    print(f"Cert Expired Check: {rot.is_expired()}")
