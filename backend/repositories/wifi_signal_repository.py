from datetime import datetime

from backend.models.wifi import Wifi

from backend.repositories.base_repository import (
    BaseRepository
)


class WifiSignalRepository(BaseRepository):

    @classmethod
    def load(cls):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            SELECT

                ssid,
                signal_dbm,
                last_seen

            FROM wifi_signal

            LIMIT 1

            """

        )

        row = cursor.fetchone()

        connection.close()

        if row is None:

            return None

        return Wifi(

            connected=False,

            ssid=row["ssid"],

            bssid=None,

            signal_dbm=row["signal_dbm"],

            started_at=None,

            last_seen=(

                datetime.fromisoformat(
                    row["last_seen"]
                )

                if row["last_seen"]

                else None

            ),

            connected_time=None

        )

    @classmethod
    def save(cls, wifi):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            INSERT OR REPLACE INTO wifi_signal (

                id,

                ssid,

                signal_dbm,

                last_seen

            )

            VALUES (

                1,

                ?, ?, ?

            )

            """,

            (

                wifi.ssid,

                wifi.signal_dbm,

                wifi.last_seen

            )

        )

        connection.commit()

        connection.close()