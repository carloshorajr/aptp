from backend.models.event import Event

from backend.repositories.sqlite_event_repository import (
    SQLiteEventRepository
)


class EventRepository:

    @classmethod
    def load(cls):

        return SQLiteEventRepository.load()

    @classmethod
    def add(cls, event: Event):

        return SQLiteEventRepository.add(event)

    @classmethod
    def clear(cls):

        return SQLiteEventRepository.clear()