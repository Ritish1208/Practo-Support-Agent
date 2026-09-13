import json
import os

MEMORY_FILE = "memory/conversation_memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_message(role, message):

    history = load_memory()

    history.append({
        "role": role,
        "message": message
    })

    with open(MEMORY_FILE, "w") as file:
        json.dump(
            history,
            file,
            indent=4
        )