from backend.core.database import Database


class DatabaseInitializer:

    @staticmethod
    def initialize():

        connection = Database.connect()

        cursor = connection.cursor()

        cursor.execute("""

            CREATE TABLE IF NOT EXISTS events (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp TEXT NOT NULL,

                level TEXT NOT NULL,

                source TEXT NOT NULL,

                message TEXT NOT NULL

            )

        """)

        connection.commit()

        connection.close()