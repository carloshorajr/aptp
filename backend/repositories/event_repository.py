import json
from dataclasses import asdict
from datetime import datetime

from backend.models.event import Event

from backend.core.paths import EVENTS_FILE

from backend.utils.datetime_utils import parse_datetime

class EventRepository:

    @classmethod
    def load(cls):

        if not EVENTS_FILE.exists():
            return []

        with open(EVENTS_FILE, "r", encoding="utf-8") as f:

            data = json.load(f)

        events = []

        for item in data:

            events.append(
                Event(
                    timestamp=parse_datetime(item["timestamp"]),
                    level=item["level"],
                    source=item["source"],
                    message=item["message"]
                )
            )

        return events
    
    @classmethod
    def add(cls, event: Event):

        events = cls.load()

        events.append(event)

        serialized = []

        for e in events:

            serialized.append({
                "timestamp": e.timestamp.isoformat(),
                "level": e.level,
                "source": e.source,
                "message": e.message
            })

        with open(EVENTS_FILE, "w", encoding="utf-8") as f:

            json.dump(
                serialized,
                f,
                indent=4,
                ensure_ascii=False
            )
    
    @classmethod
    def clear(cls):

        with open(EVENTS_FILE, "w", encoding="utf-8") as f:

            json.dump(
                [],
                f,
                indent=4,
                ensure_ascii=False
            )