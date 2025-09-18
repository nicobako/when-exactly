from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, Any, Iterable

from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.delta import Delta
from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment

if TYPE_CHECKING:
    from when_exactly.custom_intervals.day import Day
    from when_exactly.custom_intervals.minute import Minute
else:
    Minute = Any
    Day = Any


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Hour(CustomInterval):
    def __init__(self, year: int, month: int, day: int, hour: int) -> None:
        start = Moment(year, month, day, hour, 0, 0)
        stop = start + Delta(hours=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return f"Hour({self.start.year}, {self.start.month}, {self.start.day}, {self.start.hour})"

    def __str__(self) -> str:
        start = self.start
        return f"{start.year:04}-{start.month:02}-{start.day:02}T{start.hour:02}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Hour:
        return Hour(
            moment.year,
            moment.month,
            moment.day,
            moment.hour,
        )

    def minutes(self) -> Iterable[Minute]:
        minute = Minute(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            0,
        )
        for _ in range(60):
            yield minute
            minute = next(minute)

    def minute(self, minute: int) -> Minute:
        return Minute(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            minute,
        )

    def day(self) -> Day:
        return Day.from_moment(self.start)

    @property
    def next(self) -> Hour:
        return Hour.from_moment(self.stop)
