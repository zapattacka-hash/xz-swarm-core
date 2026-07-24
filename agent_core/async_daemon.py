import sys
import os
import asyncio
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_core.swarm_mesh import SwarmMesh
from math_core.phase_engine import evolve_spinor_state

class AsyncSwarmDaemon:
    def __init__(self, tick_interval: float = 0.1):
        self.mesh = SwarmMesh()
        self.tick_interval = tick_interval
        self.is_running = False

    def register_node(self, agent_id: str):
        return self.mesh.register_node(agent_id)

    async def _node_telemetry_loop(self, agent_id: str, field_vector: np.ndarray):
        """Simulates continuous non-blocking spin drift for a specific node."""
        node = self.mesh.nodes[agent_id]
        while self.is_running:
            # Continuously evolve state via Hamiltonian phase dynamics
            node.current_state = evolve_spinor_state(
                spinor=node.current_state,
                field_vector=field_vector,
                dt=self.tick_interval
            )
            await asyncio.sleep(self.tick_interval)

    async def _mesh_consensus_loop(self, consensus_interval: float = 0.5):
        """Periodically evaluates mesh consensus and realigns drifting nodes."""
        while self.is_running:
            consensus = self.mesh.compute_mesh_consensus()
            corrections = self.mesh.synchronize_mesh(correction_fraction=0.1)
            
            # Apply correction step to each node's state vector
            for agent_id, corrected_state in corrections.items():
                self.mesh.nodes[agent_id].current_state = corrected_state
                
            await asyncio.sleep(consensus_interval)

    async def run_swarm_simulation(self, duration_seconds: float = 1.5):
        """Runs concurrent node evolution and mesh synchronization tasks."""
        self.is_running = True
        
        # Field vectors driving different drift directions per node
        node_fields = {
            "node-alpha": np.array([0.1, 0.0, 0.2]),
            "node-beta":  np.array([0.8, -0.4, 0.1]),  # Fast drifting node
            "node-gamma": np.array([-0.1, 0.3, 0.0])
        }
        
        tasks = []
        for agent_id, field in node_fields.items():
            self.register_node(agent_id)
            tasks.append(asyncio.create_task(self._node_telemetry_loop(agent_id, field)))
            
        tasks.append(asyncio.create_task(self._mesh_consensus_loop()))
        
        print(f"--- Async Swarm Daemon Running ({duration_seconds}s) ---")
        await asyncio.sleep(duration_seconds)
        
        self.is_running = False
        await asyncio.gather(*tasks, return_exceptions=True)
        print("--- Daemon Execution Complete ---")

if __name__ == "__main__":
    daemon = AsyncSwarmDaemon(tick_interval=0.05)
    asyncio.run(daemon.run_swarm_simulation(duration_seconds=0.3))
    
    consensus = daemon.mesh.compute_mesh_consensus()
    print(f"Final Mesh Consensus (q_bar): {consensus}")
    print(f"Final Consensus Norm         : {np.linalg.norm(consensus):.4f}")
