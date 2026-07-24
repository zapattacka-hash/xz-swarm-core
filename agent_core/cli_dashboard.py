import sys
import os
import asyncio
import time
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_core.async_daemon import AsyncSwarmDaemon

def clear_terminal():
    """Clears terminal screen using ANSI escape sequence."""
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

async def render_dashboard(daemon: AsyncSwarmDaemon, refresh_rate: float = 0.1):
    """Renders real-time node states and drift telemetry to console."""
    start_time = time.time()
    
    # Wait until daemon starts up
    while not daemon.is_running:
        await asyncio.sleep(0.01)
        
    while daemon.is_running:
        consensus = daemon.mesh.compute_mesh_consensus()
        elapsed = time.time() - start_time
        
        output = []
        output.append("==========================================================================")
        output.append("                      XZ LABS: SWARM CORE TELEMETRY DASHBOARD             ")
        output.append(f" Uptime: {elapsed:.1f}s | Active Nodes: {len(daemon.mesh.nodes)} | Status: ACTIVE")
        output.append("==========================================================================")
        output.append(f"{'NODE ID':<12} | {'QUATERNION STATE [w, x, y, z]':<36} | {'DRIFT':<6} | {'NORM':<6}")
        output.append("--------------------------------------------------------------------------")
        
        for agent_id, node in daemon.mesh.nodes.items():
            q = node.current_state
            dot_prod = np.abs(np.dot(q, consensus))
            drift = 1.0 - np.clip(dot_prod, 0.0, 1.0)
            norm = np.linalg.norm(q)
            
            q_str = f"[{q[0]:.3f}, {q[1]:.3f}, {q[2]:.3f}, {q[3]:.3f}]"
            output.append(f"{agent_id:<12} | {q_str:<36} | {drift:.4f} | {norm:.4f}")
            
        output.append("--------------------------------------------------------------------------")
        c_str = f"[{consensus[0]:.3f}, {consensus[1]:.3f}, {consensus[2]:.3f}, {consensus[3]:.3f}]"
        c_norm = np.linalg.norm(consensus)
        output.append(f"{'MESH CONSENSUS':<12} | {c_str:<36} | 0.0000 | {c_norm:.4f}")
        output.append("==========================================================================")
        
        clear_terminal()
        print("\n".join(output))
        await asyncio.sleep(refresh_rate)

async def main():
    daemon = AsyncSwarmDaemon(tick_interval=0.05)
    
    # Run dashboard concurrently with daemon simulation loop
    dashboard_task = asyncio.create_task(render_dashboard(daemon, refresh_rate=0.1))
    simulation_task = asyncio.create_task(daemon.run_swarm_simulation(duration_seconds=2.0))
    
    await simulation_task
    # Cancel dashboard task once simulation loop finishes
    dashboard_task.cancel()
    try:
        await dashboard_task
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    asyncio.run(main())
