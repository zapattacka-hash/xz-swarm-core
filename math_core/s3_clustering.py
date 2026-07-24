import numpy as np

def cluster_states_geodesic(states: dict, max_radius_rad: float = 0.3) -> dict:
    """Groups node states into clusters based on angular distance on S^3."""
    clusters = {}
    assigned = set()
    cluster_id = 0
    
    agent_ids = list(states.keys())
    for i, id1 in enumerate(agent_ids):
        if id1 in assigned:
            continue
        cluster_members = [id1]
        assigned.add(id1)
        q1 = states[id1]
        
        for id2 in agent_ids[i+1:]:
            if id2 in assigned:
                continue
            q2 = states[id2]
            dot_val = np.clip(np.abs(np.dot(q1, q2)), 0.0, 1.0)
            dist = 2.0 * np.arccos(dot_val)
            if dist <= max_radius_rad:
                cluster_members.append(id2)
                assigned.add(id2)
                
        clusters[f"cluster_{cluster_id}"] = cluster_members
        cluster_id += 1
    return clusters

if __name__ == "__main__":
    st = {
        "n1": np.array([1.0, 0.0, 0.0, 0.0]),
        "n2": np.array([0.99, 0.01, 0.0, 0.0]),
        "n3": np.array([0.0, 1.0, 0.0, 0.0])
    }
    print("S^3 Geodesic Clusters:", cluster_states_geodesic(st))
