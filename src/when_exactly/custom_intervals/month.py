from __future__ import annotations

import dataclasses
from functools import cached_property
from typing import TYPE_CHECKING, Any

from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.delta import Delta
from when_exactly.core.helper_functions import gen_until as gen_until
from when_exactly.core.moment import Moment

if TYPE_CHECKING:
    from when_exactly.custom_collections.days import Days
    from when_exactly.custom_intervals.day import Day
else:
    Day = Any
    Days = Any


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Month(CustomInterval):
    def __init__(self, year: int, month: int) -> None:
        start = Moment(year, month, 1, 0, 0, 0)
        stop = start + Delta(months=1)
        CustomInterval.__init__(
            self,
            start=start,
            stop=stop,
        )

    def __repr__(self) -> str:
        return f"Month({self.start.year}, {self.start.month})"

    def __str__(self) -> str:
        return f"{self.start.year:04}-{self.start.month:02}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Month:
        return Month(
            moment.year,
            moment.month,
        )

    def days(self) -> Days:
        return Days(
            gen_until(
                Day(self.start.year, self.start.month, 1),
                Day(self.start.year, self.start.month + 1, 1),
            )
        )

    def day(self, day: int) -> Day:
        return Day(
            self.start.year,
            self.start.month,
            day,
        )

    @property
    def next(self) -> Month:
        return Month.from_moment(self.stop)
