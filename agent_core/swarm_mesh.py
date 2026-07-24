import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_core.orchestrator import SwarmAgentNode

class SwarmMesh:
    def __init__(self):
        self.nodes = {}

    def register_node(self, agent_id: str) -> SwarmAgentNode:
        """Registers a new agent node to the mesh."""
        node = SwarmAgentNode(agent_id)
        self.nodes[agent_id] = node
        return node

    def compute_mesh_consensus(self) -> np.ndarray:
        """
        Calculates the normalized consensus vector (mean SU(2) state)
        across all active nodes in the swarm.
        """
        if not self.nodes:
            return np.array([1.0, 0.0, 0.0, 0.0])
        
        states = [node.current_state for node in self.nodes.values()]
        mean_state = np.mean(states, axis=0)
        
        norm = np.linalg.norm(mean_state)
        if norm < 1e-6:
            return np.array([1.0, 0.0, 0.0, 0.0])
            
        return mean_state / norm

    def synchronize_mesh(self, correction_fraction: float = 0.2) -> dict:
        """
        Evaluates mesh consensus and computes correction step states
        for nodes drifting away from cluster equilibrium.
        """
        consensus = self.compute_mesh_consensus()
        corrections = {}
        
        for agent_id, node in self.nodes.items():
            step = node.compute_optimal_transition(consensus, step_fraction=correction_fraction)
            corrections[agent_id] = step
            
        return corrections

if __name__ == "__main__":
    print("--- XZ Swarm Core: Multi-Agent Mesh System ---")
    
    mesh = SwarmMesh()
    
    # 1. Register Swarm Nodes
    n1 = mesh.register_node("node-alpha")
    n2 = mesh.register_node("node-beta")
    n3 = mesh.register_node("node-gamma")
    
    # 2. Simulate Telemetry Ingestion Across Swarm
    n1.update_state_from_telemetry(cpu=0.15, latency_ms=10.0, bandwidth=0.20)
    n2.update_state_from_telemetry(cpu=0.80, latency_ms=150.0, bandwidth=0.90)  # High load outlier
    n3.update_state_from_telemetry(cpu=0.25, latency_ms=20.0, bandwidth=0.35)
    
    # 3. Compute Mesh Consensus State
    consensus_state = mesh.compute_mesh_consensus()
    print(f"Mesh Consensus State (q_bar): {consensus_state}")
    print(f"Consensus Norm Verification  : {np.linalg.norm(consensus_state):.4f}\n")
    
    # 4. Generate Synchronized Equilibrium Transitions
    correction_map = mesh.synchronize_mesh(correction_fraction=0.25)
    print("--- Individual Node Correction Steps ---")
    for agent_id, target_step in correction_map.items():
        print(f"[{agent_id}] Correction Step: {target_step}")
