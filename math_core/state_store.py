import os
import h5py
import numpy as np

class H5StateStore:
    def __init__(self, filepath: str = "swarm_telemetry.h5"):
        self.filepath = filepath
        self._init_db()

    def _init_db(self):
        """Initializes HDF5 schema with chunked, compressed datasets."""
        with h5py.File(self.filepath, "a") as h5f:
            if "timestamps" not in h5f:
                h5f.create_dataset("timestamps", shape=(0,), maxshape=(None,), dtype="f8", chunks=True)
            if "consensus" not in h5f:
                h5f.create_dataset("consensus", shape=(0, 4), maxshape=(None, 4), dtype="f4", chunks=True, compression="gzip")
            if "nodes" not in h5f:
                h5f.create_group("nodes")

    def log_snapshot(self, timestamp: float, consensus: np.ndarray, node_states: dict):
        """Appends a new trajectory snapshot to the binary store."""
        with h5py.File(self.filepath, "a") as h5f:
            # Append timestamp
            ts_ds = h5f["timestamps"]
            curr_idx = ts_ds.shape[0]
            ts_ds.resize((curr_idx + 1,))
            ts_ds[curr_idx] = timestamp
            
            # Append consensus quaternion
            c_ds = h5f["consensus"]
            c_ds.resize((curr_idx + 1, 4))
            c_ds[curr_idx] = consensus
            
            # Append individual node state trajectories
            nodes_grp = h5f["nodes"]
            for agent_id, state in node_states.items():
                if agent_id not in nodes_grp:
                    nodes_grp.create_dataset(agent_id, shape=(0, 4), maxshape=(None, 4), dtype="f4", chunks=True, compression="gzip")
                
                n_ds = nodes_grp[agent_id]
                n_ds.resize((curr_idx + 1, 4))
                n_ds[curr_idx] = state

    def load_trajectory(self, agent_id: str) -> np.ndarray:
        """Retrieves stored quaternion trajectory for a specific node."""
        with h5py.File(self.filepath, "r") as h5f:
            if "nodes" in h5f and agent_id in h5f["nodes"]:
                return h5f["nodes"][agent_id][:]
            return np.empty((0, 4))

if __name__ == "__main__":
    print("--- HDF5 Swarm State Store Test ---")
    store = H5StateStore("test_store.h5")
    
    # Simulate logging a snapshot
    t0 = 0.0
    cons = np.array([1.0, 0.0, 0.0, 0.0])
    nodes = {"node-alpha": np.array([0.99, 0.01, 0.0, 0.0])}
    
    store.log_snapshot(t0, cons, nodes)
    retrieved = store.load_trajectory("node-alpha")
    print(f"Logged State   : {nodes['node-alpha']}")
    print(f"Retrieved State: {retrieved[0]}")
    print(f"Norm Check     : {np.linalg.norm(retrieved[0]):.4f}")
    
    # Cleanup test store
    if os.path.exists("test_store.h5"):
        os.remove("test_store.h5")
