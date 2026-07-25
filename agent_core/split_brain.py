class SplitBrainDetector:
    def __init__(self, total_nodes: int = 5):
        self.total_nodes = total_nodes

    def has_quorum(self, reachable_nodes: int) -> bool:
        return reachable_nodes >= (self.total_nodes // 2 + 1)

if __name__ == "__main__":
    sbd = SplitBrainDetector(total_nodes=5)
    print(f"Quorum Maintained (3/5): {sbd.has_quorum(3)}")
    print(f"Quorum Maintained (2/5): {sbd.has_quorum(2)}")
