import os

def safe_create_dir(path):
    os.makedirs(path, exist_ok=True)
    return f"[SYSTEM] Storage ready: {path}"