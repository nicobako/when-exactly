from __future__ import annotations

import dataclasses
from functools import cached_property
from typing import TYPE_CHECKING, Any

from when_exactly.core.custom_interval import CustomInterval

if TYPE_CHECKING:
    from when_exactly.custom_intervals.hour import Hour
    from when_exactly.custom_intervals.month import Month
    from when_exactly.custom_intervals.ordinal_day import OrdinalDay
    from when_exactly.custom_intervals.week import Week
    from when_exactly.custom_intervals.weekday import Weekday
else:
    Hour = Any
    Month = Any
    OrdinalDay = Any
    Week = Any
    Weekday = Any

from when_exactly.core.delta import Delta
from when_exactly.core.moment import Moment


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Day(CustomInterval):
    """Represents a single day, from midnight to midnight."""

    def __init__(self, year: int, month: int, day: int) -> None:
        start = Moment(year, month, day, 0, 0, 0)
        stop = start + Delta(days=1)
        CustomInterval.__init__(self, start=start, stop=stop)

    @classmethod
    def from_moment(cls, moment: Moment) -> Day:
        return Day(
            moment.year,
            moment.month,
            moment.day,
        )

    @property
    def previous(self) -> Day:
        return Day.from_moment(self.start - Delta(days=1))

    def __repr__(self) -> str:
        return f"Day({self.start.year}, {self.start.month}, {self.start.day})"

    def __str__(self) -> str:
        return f"{self.start.year:04}-{self.start.month:02}-{self.start.day:02}"

    def hour(self, hour: int) -> Hour:
        return Hour(
            self.start.year,
            self.start.month,
            self.start.day,
            hour,
        )

    @cached_property
    def month(self) -> Month:
        return Month(
            self.start.year,
            self.start.month,
        )

    @cached_property
    def week(self) -> Week:
        return Week.from_moment(self.start)

    @cached_property
    def ordinal_day(self) -> OrdinalDay:
        return OrdinalDay(
            self.start.year,
            self.start.ordinal_day,
        )

    @cached_property
    def weekday(self) -> Weekday:
        return Weekday(
            self.start.year,
            self.start.week,
            self.start.week_day,
        )

    @property
    def next(self) -> Day:
        return Day.from_moment(self.stop)
