from __future__ import annotations

import dataclasses

from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.delta import Delta
from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment
from when_exactly.custom_intervals.minute import Minute


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Second(CustomInterval):
    """A second interval."""

    def __init__(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int
    ) -> None:
        start = Moment(year, month, day, hour, minute, second)
        stop = start + Delta(seconds=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return f"Second({self.start.year}, {self.start.month}, {self.start.day}, {self.start.hour}, {self.start.minute}, {self.start.second})"

    def __str__(self) -> str:
        start = self.start
        return f"{start.year:04}-{start.month:02}-{start.day:02}T{start.hour:02}:{start.minute:02}:{start.second:02}"

    def minute(self) -> Minute:
        return Minute.from_moment(self.start)

    @property
    def next(self) -> Second:
        return Second.from_moment(self.stop)

    @classmethod
    def from_moment(cls, moment: Moment) -> Second:
        return Second(
            moment.year,
            moment.month,
            moment.day,
            moment.hour,
            moment.minute,
            moment.second,
        )
