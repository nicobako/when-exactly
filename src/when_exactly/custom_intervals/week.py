from __future__ import annotations

import dataclasses
import datetime
from functools import cached_property

from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.delta import Delta
from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment
from when_exactly.custom_collections.days import Days
from when_exactly.custom_collections.weekdays import Weekdays
from when_exactly.custom_intervals.weekday import Weekday


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Week(CustomInterval):
    def __init__(self, year: int, week: int) -> None:
        start = Moment.from_datetime(datetime.datetime.fromisocalendar(year, week, 1))
        stop = start + Delta(days=7)
        Interval.__init__(
            self,
            start=start,
            stop=stop,
        )

    def __repr__(self) -> str:
        return f"Week({self.start.week_year}, {self.start.week})"

    def __str__(self) -> str:
        return f"{self.start.week_year:04}-W{self.start.week:02}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Week:
        return Week(
            moment.week_year,
            moment.week,
        )

    @property
    def next(self) -> Week:
        return Week.from_moment(self.stop)

    def week_day(self, week_day: int) -> Weekday:
        return Weekday(
            self.start.week_year,
            self.start.week,
            week_day,
        )

    @cached_property
    def week_days(self) -> Weekdays:
        return Weekdays([self.week_day(i) for i in range(1, 8)])

    @cached_property
    def days(self) -> Days:
        return Days([self.week_day(i).to_day() for i in range(1, 8)])
