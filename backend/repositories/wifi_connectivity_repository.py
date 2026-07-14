from backend.models.wifi import Wifi

from backend.repositories.base_repository import (
    BaseRepository
)

from backend.utils.datetime_utils import now

class WifiConnectivityRepository(BaseRepository):

    @classmethod
    def load(cls):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            SELECT
                connected,
                ssid,
                started_at,
                last_seen,
                connected_time
            FROM wifi_connectivity
            LIMIT 1
            """

        )

        row = cursor.fetchone()

        connection.close()

        if row is None:

            return None

        return Wifi(

            connected=bool(row["connected"]),

            ssid=row["ssid"],

            started_at=row["started_at"],

            last_seen=row["last_seen"],

            connected_time=row["connected_time"]

        )
    
    @classmethod
    def save(cls, wifi: Wifi):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            "DELETE FROM wifi_connectivity"

        )

        cursor.execute(

            """

            INSERT INTO wifi_connectivity (

                connected,

                ssid,

                started_at,

                last_seen,

                connected_time

            )

            VALUES (

                ?, ?, ?, ?, ?

            )

            """,

            (

                wifi.connected,

                wifi.ssid,

                wifi.started_at,

                wifi.last_seen,

                wifi.connected_time

            )

        )

        connection.commit()

        connection.close()
    
    @classmethod
    def clear(cls):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            "DELETE FROM wifi_connectivity"

        )

        connection.commit()

        connection.close()