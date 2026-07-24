import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_core.api_gateway import app

def export_openapi_schema(output_path: str = "openapi.json"):
    schema = app.openapi()
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)
    print(f"Exported OpenAPI schema to '{output_path}'.")

if __name__ == "__main__":
    export_openapi_schema()
