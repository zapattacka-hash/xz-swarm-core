import numpy as np

def compute_geodesic_distance(q1: np.ndarray, q2: np.ndarray) -> float:
    """Calculates angular distance on S^3 manifold between two unit quaternions."""
    dot_prod = np.abs(np.dot(q1, q2))
    dot_clipped = np.clip(dot_prod, 0.0, 1.0)
    return float(2.0 * np.arccos(dot_clipped))

class ByzantineFilter:
    def __init__(self, distance_threshold_rad: float = 0.5):
        self.distance_threshold = distance_threshold_rad
        self.quarantined_nodes = set()

    def filter_active_states(self, node_states: dict, base_consensus: np.ndarray) -> dict:
        """
        Evaluates node states against consensus manifold.
        Flags and isolates outlier nodes exceeding geodesic deviation bounds.
        """
        valid_states = {}
        for agent_id, state in node_states.items():
            if agent_id in self.quarantined_nodes:
                continue
                
            dist = compute_geodesic_distance(state, base_consensus)
            if dist > self.distance_threshold:
                print(f"[SECURITY ALERT] Node '{agent_id}' flagged as Byzantine! Deviation: {dist:.4f} rad > Threshold: {self.distance_threshold:.4f} rad.")
                self.quarantined_nodes.add(agent_id)
            else:
                valid_states[agent_id] = state
                
        return valid_states

if __name__ == "__main__":
    print("--- XZ Swarm Core: Byzantine Node Isolation Test ---")
    b_filter = ByzantineFilter(distance_threshold_rad=0.4)
    
    baseline = np.array([1.0, 0.0, 0.0, 0.0])
    test_nodes = {
        "node-valid": np.array([0.99, 0.1, 0.0, 0.0]) / np.linalg.norm([0.99, 0.1, 0.0, 0.0]),
        "node-rogue": np.array([0.50, 0.8, 0.2, 0.1]) / np.linalg.norm([0.50, 0.8, 0.2, 0.1])  # Massive drift
    }
    
    filtered = b_filter.filter_active_states(test_nodes, baseline)
    print(f"Active Valid Nodes: {list(filtered.keys())}")
    print(f"Quarantined Nodes : {list(b_filter.quarantined_nodes)}")
