from datetime import datetime

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
                bssid,
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

            bssid=row["bssid"],

            signal_dbm=None,

            started_at=(

                datetime.fromisoformat(row["started_at"])

                if row["started_at"] else None

            ),

            last_seen=(

                datetime.fromisoformat(row["last_seen"])

                if row["last_seen"] else None

            ),

            connected_time=row["connected_time"]

        )
            
    @classmethod
    def save(cls, wifi: Wifi):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            INSERT OR REPLACE INTO wifi_connectivity (
                id,
                connected,
                ssid,
                bssid,
                started_at,
                last_seen,
                connected_time
            )

            VALUES (

                1,

                ?, ?, ?, ?, ?, ?

            )

            """,

            (

                int(wifi.connected),

                wifi.ssid,

                wifi.bssid,

                wifi.started_at,

                wifi.last_seen,

                wifi.connected_time

            )

        )

        connection.commit()

        connection.close()        