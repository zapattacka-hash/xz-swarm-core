import numpy as np

class MeshTopology:
    def __init__(self, node_ids: list):
        self.nodes = node_ids
        self.n = len(node_ids)
        self.adjacency = np.ones((self.n, self.n)) - np.eye(self.n)  # Fully connected mesh default

    def set_edge(self, idx1: int, idx2: int, weight: float):
        self.adjacency[idx1, idx2] = weight
        self.adjacency[idx2, idx1] = weight

    def get_neighbors(self, idx: int) -> np.ndarray:
        return self.adjacency[idx]

if __name__ == "__main__":
    topo = MeshTopology(["alpha", "beta", "gamma"])
    print("Mesh Adjacency Matrix:\n", topo.adjacency)
