import sqlite3

from backend.core.paths import DATA_DIR


DATABASE_FILE = DATA_DIR / "aptp.db"


class Database:

    @staticmethod
    def connect():

        DATA_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        connection = sqlite3.connect(
            DATABASE_FILE
        )

        connection.row_factory = sqlite3.Row

        return connection