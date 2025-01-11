from __future__ import annotations

import dataclasses
import datetime
from typing import Iterable

from when_exactly.delta import Delta
from when_exactly.interval import Interval
from when_exactly.moment import Moment


def now() -> Moment:
    return Moment.from_datetime(datetime.datetime.now())


def second(
    year: int, month: int, day: int, hour: int, minute: int, second: int
) -> Second:
    start = Moment(year, month, day, hour, minute, second).to_datetime()
    stop = start + datetime.timedelta(seconds=1)
    return Second(
        start=Moment.from_datetime(start),
        stop=Moment.from_datetime(stop),
    )


_second = second


def minute(year: int, month: int, day: int, hour: int, minute: int) -> Minute:
    start = Moment(year, month, day, hour, minute, 0)
    stop = start.to_datetime() + datetime.timedelta(minutes=1)
    return Minute(
        start=start,
        stop=Moment.from_datetime(stop),
    )


_minute = minute


def hour(year: int, month: int, day: int, hour: int) -> Hour:
    start = Moment(year, month, day, hour, 0, 0)
    stop = start.to_datetime() + datetime.timedelta(hours=1)
    return Hour(
        start=start,
        stop=Moment.from_datetime(stop),
    )


_hour = hour


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

    def __next__(self) -> Interval:
        return Hour(
            start=self.stop,
            stop=self.stop + Delta(hours=1),
        )
