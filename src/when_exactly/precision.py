import dataclasses
from enum import Enum

from when_exactly.delta import Delta


@dataclasses.dataclass(frozen=True)
class Precision:
    level: int
    name: str
    delta: Delta


class Precisions(Enum):
    """Precision levels for date and time intervals."""

    SECOND = Precision(1, "second", Delta(seconds=1))
    MINUTE = Precision(2, "minute", Delta(minutes=1))
    HOUR = Precision(3, "hour", Delta(hours=1))
    DAY = Precision(4, "day", Delta(days=1))
    WEEK = Precision(5, "week", Delta(weeks=1))
    MONTH = Precision(6, "month", Delta(months=1))
    YEAR = Precision(7, "year", Delta(years=1))
