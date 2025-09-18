from __future__ import annotations

import dataclasses
import datetime

from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.delta import Delta
from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class OrdinalDay(CustomInterval):
    """An ordinal day interval."""

    def __init__(self, year: int, ordinal_day: int) -> None:
        start = Moment.from_datetime(
            datetime.datetime.fromordinal(
                datetime.date(year, 1, 1).toordinal() + ordinal_day - 1
            )
        )
        stop = start + Delta(days=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return f"OrdinalDay({self.start.year}, {self.start.ordinal_day})"

    def __str__(self) -> str:
        return f"{self.start.year:04}-{self.start.ordinal_day:03}"

    @classmethod
    def from_moment(cls, moment: Moment) -> OrdinalDay:
        return OrdinalDay(moment.year, moment.ordinal_day)

    @property
    def next(self) -> OrdinalDay:
        return OrdinalDay.from_moment(self.stop)
