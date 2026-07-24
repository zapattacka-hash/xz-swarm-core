import sys
import os
import pytest
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math_core.state_mapper import metrics_to_spinor
from math_core.spinor_opt import optimize_spinor_step
from agent_core.swarm_mesh import SwarmMesh

def test_metrics_to_spinor_normalization():
    """Assert that any telemetry input yields a strictly unit-normalized spinor."""
    spinor = metrics_to_spinor(cpu_load=0.99, latency_ms=850.0, bandwidth_usage=0.12)
    assert np.isclose(np.linalg.norm(spinor), 1.0, atol=1e-6)

def test_spinor_opt_double_cover_sign_inversion():
    """Assert SLERP correctly handles negative dot product (double-cover shortest path)."""
    q1 = np.array([1.0, 0.0, 0.0, 0.0])
    q2 = np.array([-0.707, 0.0, 0.707, 0.0])  # Opposite sign orientation
    
    midpoint = optimize_spinor_step(q1, q2, 0.5)
    assert np.isclose(np.linalg.norm(midpoint), 1.0, atol=1e-6)
    # Ensure w component remains positive due to phase inversion
    assert midpoint[0] > 0.0

def test_mesh_consensus_calculation():
    """Assert mesh consensus accurately computes normalized mean state across multi-nodes."""
    mesh = SwarmMesh()
    n1 = mesh.register_node("node-1")
    n2 = mesh.register_node("node-2")
    
    n1.update_state_from_telemetry(cpu=0.10, latency_ms=10.0, bandwidth=0.10)
    n2.update_state_from_telemetry(cpu=0.90, latency_ms=500.0, bandwidth=0.90)
    
    consensus = mesh.compute_mesh_consensus()
    assert len(consensus) == 4
    assert np.isclose(np.linalg.norm(consensus), 1.0, atol=1e-6)

from math_core.phase_engine import evolve_spinor_state

def test_hamiltonian_spin_evolution_norm():
    """Assert Hamiltonian spin evolution preserves unit norm over continuous time."""
    initial = np.array([1.0, 0.0, 0.0, 0.0])
    field = np.array([0.5, -1.2, 0.3])
    evolved = evolve_spinor_state(initial, field, dt=1.5)
    assert np.isclose(np.linalg.norm(evolved), 1.0, atol=1e-6)

from agent_core.async_daemon import AsyncSwarmDaemon

@pytest.mark.asyncio
async def test_async_daemon_execution_norm():
    """Assert async daemon runs concurrently and maintains unit norm consensus."""
    daemon = AsyncSwarmDaemon(tick_interval=0.01)
    await daemon.run_swarm_simulation(duration_seconds=0.1)
    consensus = daemon.mesh.compute_mesh_consensus()
    assert np.isclose(np.linalg.norm(consensus), 1.0, atol=1e-6)
