import json
from datetime import datetime

FILE = "data.json"

def save_session(task, duration):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({
        "task": task,
        "duration_min": duration,
        "date": datetime.now().isoformat()
    })

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
