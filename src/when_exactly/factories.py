from __future__ import annotations

import dataclasses
import datetime
from typing import Iterable

from when_exactly.delta import Delta
from when_exactly.interval import Interval
from when_exactly.intervals import Intervals
from when_exactly.moment import Moment


def now() -> Moment:
    return Moment.from_datetime(datetime.datetime.now())


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class CustomInterval(Interval):
    def __init__(self, *args: int, **kwargs: int):
        raise NotImplementedError("CustomInterval init not implemented")

    def __repr__(self) -> str:
        raise NotImplementedError("CustomInterval repr not implemented")

    @classmethod
    def from_moment(cls, moment: Moment) -> CustomInterval:
        raise NotImplementedError("CustomInterval from_moment not implemented")

    def __next__(self) -> CustomInterval:
        raise NotImplementedError("CustomInterval next not implemented")


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Second(CustomInterval):
    def __init__(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int
    ) -> None:
        start = Moment(year, month, day, hour, minute, second)
        stop = start + Delta(seconds=1)
        Interval.__init__(self, start=start, stop=stop)

    def minute(self) -> Minute:
        return Minute(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            self.start.minute,
        )

    def __next__(self) -> Second:
        return Second(
            self.stop.year,
            self.stop.month,
            self.stop.day,
            self.stop.hour,
            self.stop.minute,
            self.stop.second,
        )

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


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Minute(CustomInterval):

    def __init__(self, year: int, month: int, day: int, hour: int, minute: int) -> None:
        start = Moment(year, month, day, hour, minute, 0)
        stop = start + Delta(minutes=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return f"Minute({self.start.year}, {self.start.month}, {self.start.day}, {self.start.hour}, {self.start.minute})"

    def seconds(self) -> Iterable[Second]:
        second = Second(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            self.start.minute,
            0,
        )
        for _ in range(60):
            yield second
            second = next(second)

    def second(self, second: int) -> Second:
        return Second(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            self.start.minute,
            second,
        )

    def __next__(self) -> Minute:
        return Minute(
            self.stop.year,
            self.stop.month,
            self.stop.day,
            self.stop.hour,
            self.stop.minute,
        )


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Hour(CustomInterval):
    def __init__(self, year: int, month: int, day: int, hour: int) -> None:
        start = Moment(year, month, day, hour, 0, 0)
        stop = start + Delta(hours=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return f"Hour({self.start.year}, {self.start.month}, {self.start.day}, {self.start.hour})"

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
        return Day(
            self.start.year,
            self.start.month,
            self.start.day,
        )

    def __next__(self) -> Hour:
        return Hour(
            self.stop.year,
            self.stop.month,
            self.stop.day,
            self.stop.hour,
        )


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Day(CustomInterval):
    def __init__(self, year: int, month: int, day: int) -> None:
        start = Moment(year, month, day, 0, 0, 0)
        stop = start + Delta(days=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return f"Day({self.start.year}, {self.start.month}, {self.start.day})"

    def hours(self) -> Iterable[Hour]:
        hour = Hour(
            self.start.year,
            self.start.month,
            self.start.day,
            0,
        )
        for _ in range(24):
            yield hour
            hour = next(hour)

    def hour(self, hour: int) -> Hour:
        return Hour(
            self.start.year,
            self.start.month,
            self.start.day,
            hour,
        )

    def month(self) -> Month:
        return Month(
            self.start.year,
            self.start.month,
        )

    def iso(self) -> str:
        return f"{self.start.year:04}-{self.start.month:02}-{self.start.day:02}"

    def __next__(self) -> Day:
        return Day(
            self.stop.year,
            self.stop.month,
            self.stop.day,
        )


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Month(Interval):

    def __init__(self, year: int, month: int) -> None:
        start = Moment(year, month, 1, 0, 0, 0)
        stop = start + Delta(months=1)
        Interval.__init__(
            self,
            start=start,
            stop=stop,
        )

    def __repr__(self) -> str:
        return f"Month({self.start.year}, {self.start.month})"

    def days(self) -> Days:
        return Days(
            filter(
                lambda d: d.start.month == self.start.month,
                [
                    Day(
                        self.start.year,
                        self.start.month,
                        i + 1,
                    )
                    for i in range(31)
                ],
            )
        )

    def day(self, day: int) -> Day:
        return Day(
            self.start.year,
            self.start.month,
            day,
        )

    def __next__(self) -> Month:
        return Month(
            self.stop.year,
            self.stop.month,
        )

    def iso(self) -> str:
        return f"{self.start.year:04}-{self.start.month:02}"


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Year(CustomInterval):

    def __init__(self, year: int) -> None:

        Interval.__init__(
            self,
            start=Moment(year, 1, 1, 0, 0, 0),
            stop=Moment(year + 1, 1, 1, 0, 0, 0),
        )

    def __repr__(self) -> str:
        return f"Year({self.start.year})"

    def months(self) -> Months:
        return Months([Month(self.start.year, self.start.month + i) for i in range(12)])

    def month(self, month: int) -> Month:
        return Month(
            self.start.year,
            month,
        )

    def __next__(self) -> Year:
        return Year(self.stop.year)

    def iso(self) -> str:
        return f"{self.start.year}"


class Days(Intervals[Day]):

    def months(self) -> Months:
        return Months([day.month() for day in self])


class Months(Intervals[Month]):
    pass
