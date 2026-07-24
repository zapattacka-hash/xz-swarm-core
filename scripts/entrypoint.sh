#!/bin/bash
set -e

echo "=== Running Container Pre-Start Checks ==="
pytest -v

echo "=== Launching XZ Swarm Core API Gateway ==="
exec uvicorn agent_core.api_gateway:app --host 0.0.0.0 --port 8000
