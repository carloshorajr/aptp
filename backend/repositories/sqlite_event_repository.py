from backend.core.database import Database

from backend.models.event import Event

from backend.utils.datetime_utils import parse_datetime

from backend.repositories.base_repository import BaseRepository


class SQLiteEventRepository(BaseRepository):

    @classmethod
    def add(cls, event: Event):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            INSERT INTO events (

                timestamp,
                level,
                source,
                message

            )

            VALUES (?, ?, ?, ?)
            """,

            (

                event.timestamp.isoformat(),
                event.level,
                event.source,
                event.message

            )

        )

        connection.commit()

        connection.close()

    @classmethod
    def load(cls):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT

                timestamp,
                level,
                source,
                message

            FROM events

            ORDER BY timestamp

        """)

        rows = cursor.fetchall()

        connection.close()

        events = []

        for row in rows:

            events.append(

                Event(

                    timestamp=parse_datetime(
                        row["timestamp"]
                    ),

                    level=row["level"],

                    source=row["source"],

                    message=row["message"]

                )

            )

        return events
    
    @classmethod
    def count(cls):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT COUNT(*)

            FROM events

        """)

        total = cursor.fetchone()[0]

        connection.close()

        return total

    @classmethod
    def clear(cls):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute("""

            DELETE FROM events

        """)

        connection.commit()

        connection.close()    
