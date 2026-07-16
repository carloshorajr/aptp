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
    def load(
        cls,
        filters_sql=None,
        params=None,
        order_by="timestamp DESC",
        limit=None
    ):

        connection = cls.connection()

        cursor = connection.cursor()

        query = """

            SELECT

                timestamp,
                level,
                source,
                message

            FROM events

        """

        parameters = list(params) if params else []

        if filters_sql:

            query += f"\nWHERE {filters_sql}"

        query += f"\nORDER BY {order_by}"

        if limit is not None:

            query += "\nLIMIT ?"

            parameters.append(limit)

        cursor.execute(
            query,
            parameters
        )

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
    def wifi_connectivity(cls):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                DATE(timestamp) AS day,
                SUM(
                    CASE
                        WHEN source = 'WiFi'
                        AND level = 'INFO'
                        AND message LIKE 'Associado%'
                        THEN 1
                        ELSE 0
                    END
                ) AS associations,
                SUM(
                    CASE
                        WHEN source = 'WiFi'
                        AND level = 'WARNING'
                        AND message LIKE 'Desassociado%'
                        THEN 1
                        ELSE 0
                    END
                ) AS disassociations
            FROM events
            GROUP BY DATE(timestamp)
            ORDER BY DATE(timestamp)
            """
        )

        rows = cursor.fetchall()

        connection.close()

        data = []

        for row in rows:

            year, month, day = row["day"].split("-")

            data.append(

                {

                    "day": f"{day}/{month}/{year}",

                    "associations": row["associations"],

                    "disassociations": row["disassociations"]

                }

            )

        return data

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