from backend.models.event import Event

from backend.repositories.sqlite_event_repository import (
    SQLiteEventRepository
)


class EventRepository:

    @classmethod
    def load(
        cls,
        filters_sql=None,
        params=None,
        order_by="timestamp DESC",
        limit=None
    ):

        return SQLiteEventRepository.load(
            filters_sql=filters_sql,
            params=params,
            order_by=order_by,
            limit=limit
        )

    @classmethod
    def add(cls, event: Event):

        return SQLiteEventRepository.add(event)

    @classmethod
    def clear(cls):

        return SQLiteEventRepository.clear()

    @classmethod
    def wifi_connectivity(cls):

        return SQLiteEventRepository.wifi_connectivity()