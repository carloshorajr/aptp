from backend.core.database import Database


class DatabaseInitializer:

    @staticmethod
    def initialize():

        connection = Database.connect()

        cursor = connection.cursor()

        #
        # Eventos
        #

        cursor.execute("""

            CREATE TABLE IF NOT EXISTS events (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp TEXT NOT NULL,

                level TEXT NOT NULL,

                source TEXT NOT NULL,

                message TEXT NOT NULL

            )

        """)

        #
        # Configuração das métricas
        #

        cursor.execute("""

            CREATE TABLE IF NOT EXISTS wifi_metric_settings (

                metric TEXT PRIMARY KEY,

                enabled INTEGER NOT NULL,

                interval_seconds INTEGER NOT NULL

            )

        """)

        #
        # Valor padrão
        #

        cursor.execute("""

            INSERT OR IGNORE INTO wifi_metric_settings (

                metric,

                enabled,

                interval_seconds

            )

            VALUES (

                'connectivity',

                1,

                60

            )

        """)

        connection.commit()

        connection.close()