import sys
import os
import numpy as np

# Ensure math_core can be imported cleanly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math_core.state_mapper import metrics_to_spinor
from math_core.spinor_opt import optimize_spinor_step

class SwarmAgentNode:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.current_state = np.array([1.0, 0.0, 0.0, 0.0]) # Baseline identity spinor

    def update_state_from_telemetry(self, cpu: float, latency_ms: float, bandwidth: float):
        """Maps incoming metrics to SU(2) state."""
        self.current_state = metrics_to_spinor(cpu_load=cpu, latency_ms=latency_ms, bandwidth_usage=bandwidth)

    def compute_optimal_transition(self, target_state: np.ndarray, step_fraction: float = 0.5) -> np.ndarray:
        """Calculates optimal short-path geodesic to target state."""
        return optimize_spinor_step(self.current_state, target_state, step_fraction)

if __name__ == "__main__":
    print("--- XZ Swarm Core: Orchestrator Engine ---")
    
    # Initialize Node Alpha
    node_alpha = SwarmAgentNode("agent-alpha")
    node_alpha.update_state_from_telemetry(cpu=0.20, latency_ms=15.0, bandwidth=0.30)
    print(f"Node Alpha Current State: {node_alpha.current_state}")
    
    # Initialize Target Telemetry (e.g., load surge on Node Beta)
    target_spinor = metrics_to_spinor(cpu_load=0.85, latency_ms=120.0, bandwidth_usage=0.95)
    print(f"Target System State    : {target_spinor}")
    
    # Calculate Phase-Correct Geodesic Trajectory Step
    step_state = node_alpha.compute_optimal_transition(target_spinor, step_fraction=0.5)
    print(f"Optimized Midpoint Step: {step_state}")
    print(f"Step Norm Verification : {np.linalg.norm(step_state):.4f}")
