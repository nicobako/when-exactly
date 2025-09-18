from __future__ import annotations

import dataclasses
import datetime
from functools import cached_property
from typing import TYPE_CHECKING, Any

from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.delta import Delta
from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment

if TYPE_CHECKING:
    from when_exactly.custom_intervals.day import Day
    from when_exactly.custom_intervals.week import Week
else:
    Day = Any
    Week = Any


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Weekday(CustomInterval):
    """A weekday interval."""

    def __init__(self, year: int, week: int, week_day: int):
        start = Moment.from_datetime(
            datetime.datetime.fromisocalendar(
                year=year,
                week=week,
                day=week_day,
            )
        )
        stop = start + Delta(days=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return (
            f"Weekday({self.start.week_year}, {self.start.week}, {self.start.week_day})"
        )

    def __str__(self) -> str:
        return f"{self.start.week_year}-W{self.start.week:02}-{self.start.week_day}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Weekday:
        return Weekday(
            year=moment.week_year,
            week=moment.week,
            week_day=moment.week_day,
        )

    @property
    def next(self) -> Weekday:
        return Weekday.from_moment(moment=self.stop)

    @cached_property
    def week(self) -> Week:
        return Week.from_moment(self.start)

    def to_day(self) -> Day:
        return Day.from_moment(self.start)
