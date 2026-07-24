import time

class TokenBucketRateLimiter:
    def __init__(self, capacity: int = 100, refill_rate: float = 10.0):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def consume(self, tokens: int = 1) -> bool:
        now = time.time()
        delta = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + delta * self.refill_rate)
        self.last_refill = now
        
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

if __name__ == "__main__":
    limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)
    print(f"Request Allowed: {limiter.consume(1)}")
