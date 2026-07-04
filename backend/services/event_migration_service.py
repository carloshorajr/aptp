from backend.repositories.event_repository import EventRepository

from backend.repositories.sqlite_event_repository import (
    SQLiteEventRepository
)


class EventMigrationService:

    @staticmethod
    def migrate():

        if SQLiteEventRepository.count() > 0:

            return

        events = EventRepository.load()

        if not events:

            return

        for event in events:

            SQLiteEventRepository.add(event)