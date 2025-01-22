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


def second(
    year: int, month: int, day: int, hour: int, minute: int, second: int
) -> Second:
    start = Moment(year, month, day, hour, minute, second)
    stop = start + Delta(seconds=1)
    return Second(
        start=start,
        stop=stop,
    )


_second = second


def minute(year: int, month: int, day: int, hour: int, minute: int) -> Minute:
    start = Moment(year, month, day, hour, minute, 0)
    stop = start + Delta(minutes=1)
    return Minute(
        start=start,
        stop=stop,
    )


_minute = minute


def hour(year: int, month: int, day: int, hour: int) -> Hour:
    start = Moment(year, month, day, hour, 0, 0)
    stop = start + Delta(hours=1)
    return Hour(
        start=start,
        stop=stop,
    )


_hour = hour


def day(year: int, month: int, day: int) -> Day:
    start = Moment(year, month, day, 0, 0, 0)
    stop = start + Delta(days=1)
    return Day(
        start=start,
        stop=stop,
    )


_day = day


def month(year: int, month: int) -> Month:
    start = Moment(year, month, 1, 0, 0, 0)
    stop = start + Delta(months=1)
    return Month(
        start=start,
        stop=stop,
    )


_month = month


def year(year: int) -> Year:
    start = Moment(year, 1, 1, 0, 0, 0)
    stop = start + Delta(years=1)
    return Year(
        start=start,
        stop=stop,
    )


_year = year


@dataclasses.dataclass(frozen=True)
class Second(Interval):
    pass

    def minute(self) -> Minute:
        return minute(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            self.start.minute,
        )

    def __next__(self) -> Second:
        return Second(
            start=self.stop,
            stop=self.stop + Delta(seconds=1),
        )


@dataclasses.dataclass(frozen=True)
class Minute(Interval):
    pass

    def seconds(self) -> Iterable[Second]:
        second = _second(
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
        return _second(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            self.start.minute,
            second,
        )

    def __next__(self) -> Minute:
        return Minute(
            start=self.stop,
            stop=self.stop + Delta(minutes=1),
        )


@dataclasses.dataclass(frozen=True)
class Hour(Interval):
    pass

    def minutes(self) -> Iterable[Minute]:
        minute = _minute(
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
        return _minute(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            minute,
        )

    def day(self) -> Day:
        return _day(
            self.start.year,
            self.start.month,
            self.start.day,
        )

    def __next__(self) -> Hour:
        return Hour(
            start=self.stop,
            stop=self.stop + Delta(hours=1),
        )


@dataclasses.dataclass(frozen=True)
class Day(Interval):

    def hours(self) -> Iterable[Hour]:
        hour = _hour(
            self.start.year,
            self.start.month,
            self.start.day,
            0,
        )
        for _ in range(24):
            yield hour
            hour = next(hour)

    def hour(self, hour: int) -> Hour:
        return _hour(
            self.start.year,
            self.start.month,
            self.start.day,
            hour,
        )

    def month(self) -> Month:
        return _month(
            self.start.year,
            self.start.month,
        )

    def __next__(self) -> Day:
        return Day(
            start=self.stop,
            stop=self.stop + Delta(days=1),
        )


@dataclasses.dataclass(frozen=True)
class Month(Interval):

    def days(self) -> Iterable[Day]:
        day = _day(
            self.start.year,
            self.start.month,
            1,
        )
        for _ in range(31):
            yield day
            day = next(day)

    def day(self, day: int) -> Day:
        return _day(
            self.start.year,
            self.start.month,
            day,
        )

    def __next__(self) -> Month:
        return Month(
            start=self.stop,
            stop=self.stop + Delta(months=1),
        )


@dataclasses.dataclass(frozen=True)
class Year(Interval):

    def months(self) -> Iterable[Month]:
        month = _month(
            self.start.year,
            1,
        )
        for _ in range(12):
            yield month
            month = next(month)

    def month(self, month: int) -> Month:
        return _month(
            self.start.year,
            month,
        )

    def __next__(self) -> Year:
        return Year(
            start=self.stop,
            stop=self.stop + Delta(years=1),
        )


def days(days: list[Day]) -> Days:
    return Days(
        days,
    )


class Days(Intervals[Day]):

    def months(self) -> Months:
        return Months(list(set([day.month() for day in self])))


class Months(Intervals[Month]):
    pass
