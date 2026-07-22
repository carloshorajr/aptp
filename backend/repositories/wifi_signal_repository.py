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

    @classmethod
    def save_history(
        cls,
        wifi
    ):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            INSERT INTO wifi_signal_history (

                signal_dbm,

                collected_at

            )

            VALUES (?, ?)
            """,

            (

                wifi.signal_dbm,

                wifi.last_seen

            )

        )

        connection.commit()

        connection.close()

    @classmethod
    def load_history(
        cls,
        limit=24
    ):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            SELECT

                signal_dbm,

                collected_at

            FROM wifi_signal_history

            ORDER BY collected_at DESC

            LIMIT ?
            """,

            (

                limit,

            )

        )

        rows = cursor.fetchall()

        connection.close()

        return list(

            reversed(

                [

                    {

                        "signal_dbm": row["signal_dbm"],

                        "time": row["collected_at"][11:16]

                    }

                    for row in rows

                ]

            )

        )

    @classmethod
    def load_latency(cls):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            SELECT

                gateway,

                rtt_avg_ms,

                loss_percent,

                last_seen

            FROM wifi_latency

            LIMIT 1

            """

        )

        row = cursor.fetchone()

        connection.close()

        if row is None:

            return None

        return {

            "gateway": row["gateway"],

            "rtt_avg_ms": row["rtt_avg_ms"],

            "loss_percent": row["loss_percent"],

            "last_seen": (

                datetime.fromisoformat(

                    row["last_seen"]

                )

                if row["last_seen"]

                else None

            )

        }

    @classmethod
    def save_latency(

        cls,

        latency

    ):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            INSERT OR REPLACE INTO wifi_latency (

                id,

                gateway,

                rtt_avg_ms,

                loss_percent,

                last_seen

            )

            VALUES (

                1,

                ?, ?, ?, ?

            )

            """,

            (

                latency["gateway"],

                latency["rtt_avg_ms"],

                latency["loss_percent"],

                latency["last_seen"]

            )

        )

        connection.commit()

        connection.close()