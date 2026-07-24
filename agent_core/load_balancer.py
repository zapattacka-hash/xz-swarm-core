class ClusterLoadBalancer:
    def __init__(self, workers: list):
        self.workers = workers
        self.index = 0

    def get_next_worker(self) -> str:
        worker = self.workers[self.index]
        self.index = (self.index + 1) % len(self.workers)
        return worker

if __name__ == "__main__":
    lb = ClusterLoadBalancer(["worker-1", "worker-2", "worker-3"])
    print(f"Assigned Worker: {lb.get_next_worker()}")
    print(f"Assigned Worker: {lb.get_next_worker()}")
