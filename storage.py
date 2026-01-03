import json
import os

DATA_FILE = "expenses.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"last_id": 0, "expenses": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
