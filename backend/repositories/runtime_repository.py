import json

from backend.core.paths import DATA_DIR


class RuntimeRepository:

    FILE = DATA_DIR / "runtime.json"

    @classmethod
    def load(cls):

        if not cls.FILE.exists():

            return {
                "boot_id": "",
                "hostname": "",
                "last_boot": ""
            }

        with open(cls.FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    @classmethod
    def save(cls, data):

        with open(cls.FILE, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )