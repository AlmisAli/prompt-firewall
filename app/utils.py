import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/scan_logs.json")


def log_scan(result: dict):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "result": result
    }

    if LOG_FILE.exists():
        data = json.loads(LOG_FILE.read_text())
    else:
        data = []

    data.append(log_entry)
    LOG_FILE.write_text(json.dumps(data, indent=2))