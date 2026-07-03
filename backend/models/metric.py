from dataclasses import dataclass
from datetime import datetime

@dataclass
class Metric:

    name: str

    value: float

    unit: str

    timestamp: datetime