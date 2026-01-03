import json
from pathlib import Path

def load_data(path):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except json.JSONDecodeError:
            return {"users": []}
    return {"users": []}

def save_data(path, data):
    path.write_text(json.dumps(data, indent=2))
