import sys
import os
import asyncio
import numpy as np
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_core.async_daemon import AsyncSwarmDaemon

daemon = AsyncSwarmDaemon(tick_interval=0.05)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Boot swarm simulation task on server startup
    sim_task = asyncio.create_task(daemon.run_swarm_simulation(duration_seconds=3600.0))
    yield
    # Cleanup task on server shutdown
    daemon.is_running = False
    sim_task.cancel()

app = FastAPI(title="XZ Swarm Core Telemetry API", version="1.0.0", lifespan=lifespan)

@app.get("/status")
async def get_status():
    """Returns general health and active node metadata."""
    return {
        "status": "ACTIVE" if daemon.is_running else "IDLE",
        "node_count": len(daemon.mesh.nodes),
        "nodes": list(daemon.mesh.nodes.keys())
    }

@app.get("/consensus")
async def get_consensus():
    """Returns current SU(2) mesh consensus quaternion vector and norm."""
    consensus = daemon.mesh.compute_mesh_consensus()
    return {
        "consensus": consensus.tolist(),
        "norm": float(np.linalg.norm(consensus))
    }

@app.websocket("/ws/telemetry")
async def websocket_telemetry_endpoint(websocket: WebSocket):
    """Broadcasting real-time node telemetry states over WebSocket stream."""
    await websocket.accept()
    try:
        while True:
            if daemon.is_running:
                consensus = daemon.mesh.compute_mesh_consensus()
                nodes_payload = {}
                for agent_id, node in daemon.mesh.nodes.items():
                    nodes_payload[agent_id] = {
                        "state": node.current_state.tolist(),
                        "norm": float(np.linalg.norm(node.current_state))
                    }
                
                payload = {
                    "consensus": consensus.tolist(),
                    "nodes": nodes_payload
                }
                await websocket.send_json(payload)
            await asyncio.sleep(0.1)
    except WebSocketDisconnect:
        pass
