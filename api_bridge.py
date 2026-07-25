#!/usr/bin/env python3
# XZ Labs: Telemetry API Bridge
import os
import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = os.path.join(os.path.dirname(__file__), '02-termux-intel', 'xz_graymarket_ledger.db')

GEO_MAP = {
    "USA": [37.0, -95.7],
    "China": [35.8, 104.1],
    "Switzerland": [46.8, 8.2],
    "Dubai Transit": [25.2, 55.2],
    "Istanbul Transit": [41.0, 28.9],
    "Tehran Assembly": [35.6, 51.3]
}

@app.route('/api/telemetry', methods=['GET'])
def get_telemetry():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT component, origin, transit_hub, timestamp FROM hardware_routes")
        rows = c.fetchall()
        conn.close()
        
        payload = []
        for row in rows:
            payload.append({
                "component": row[0],
                "origin": row[1],
                "origin_coords": GEO_MAP.get(row[1], [0,0]),
                "transit": row[2],
                "transit_coords": GEO_MAP.get(row[2], [0,0])
            })
        return jsonify({"status": "active", "data": payload})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    print("[*] XZ Labs Telemetry Bridge Active on Port 5000")
    app.run(port=5000)