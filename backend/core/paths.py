from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = ROOT_DIR / "data"

SETTINGS_FILE = DATA_DIR / "settings.json"

RUNTIME_FILE = DATA_DIR / "runtime.json"

DATABASE_FILE = DATA_DIR / "aptp.db"