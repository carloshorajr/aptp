from backend.repositories.base_repository import BaseRepository


class WifiMetricSettingsRepository(BaseRepository):

    @classmethod
    def load(cls, metric):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            SELECT *

            FROM wifi_metric_settings

            WHERE metric = ?

            """,

            (metric,)

        )

        row = cursor.fetchone()

        connection.close()

        return row

    @classmethod
    def save(

        cls,

        metric,

        enabled,

        interval_seconds

    ):

        connection = cls.connection()

        cursor = connection.cursor()

        cursor.execute(

            """

            UPDATE wifi_metric_settings

            SET

                enabled = ?,

                interval_seconds = ?

            WHERE metric = ?

            """,

            (

                enabled,

                interval_seconds,

                metric

            )

        )

        connection.commit()

        connection.close()