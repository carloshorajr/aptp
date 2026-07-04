from backend.core.database import Database


class BaseRepository:

    @staticmethod
    def connection():

        return Database.connect()