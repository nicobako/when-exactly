from __future__ import annotations

import dataclasses
import datetime
from typing import Callable, Generator, Iterable, Protocol, TypeVar

from when_exactly.core.delta import Delta
from when_exactly.interval import Interval
from when_exactly.intervals import Intervals
from when_exactly.core.moment import Moment


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

    def __str__(self) -> str:
        raise NotImplementedError("CustomInterval str not implemented")


class Nextable(Protocol):
    def __next__(self) -> Nextable: ...

    start: Moment


def get_n_next(n: int, interval: Nextable) -> Generator[Nextable, None, None]:
    for _ in range(n):
        yield interval
        interval = next(interval)


C = TypeVar("C", bound=CustomInterval)


def get_next_while(
    interval: C, condition: Callable[[C], bool]
) -> Generator[C, None, None]:
    while condition(interval):
        yield interval
        interval = next(interval)  # type: ignore


# def get_next_while(
#     interval: Nextable, condition: Callable[[Nextable], bool]
# ) -> Generator[Nextable, None, None]:
#     while condition(interval):
#         yield interval
#         interval = next(interval)


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

    def __next__(self) -> Second:
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


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Minute(CustomInterval):

    def __init__(self, year: int, month: int, day: int, hour: int, minute: int) -> None:
        start = Moment(year, month, day, hour, minute, 0)
        stop = start + Delta(minutes=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return f"Minute({self.start.year}, {self.start.month}, {self.start.day}, {self.start.hour}, {self.start.minute})"

    def __str__(self) -> str:
        start = self.start
        return f"{start.year:04}-{start.month:02}-{start.day:02}T{start.hour:02}:{start.minute:02}"

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
        return Minute.from_moment(self.stop)

    @classmethod
    def from_moment(cls, moment: Moment) -> Minute:
        return Minute(
            moment.year,
            moment.month,
            moment.day,
            moment.hour,
            moment.minute,
        )


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

    def __next__(self) -> Hour:
        return Hour.from_moment(self.stop)


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Day(CustomInterval):
    def __init__(self, year: int, month: int, day: int) -> None:
        start = Moment(year, month, day, 0, 0, 0)
        stop = start + Delta(days=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        return f"Day({self.start.year}, {self.start.month}, {self.start.day})"

    def __str__(self) -> str:
        return f"{self.start.year:04}-{self.start.month:02}-{self.start.day:02}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Day:
        return Day(
            moment.year,
            moment.month,
            moment.day,
        )

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

    def week(self) -> Week:
        return Week.from_moment(self.start)

    def __next__(self) -> Day:
        return Day.from_moment(self.stop)


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
        return f"Week({self.start.iso_year}, {self.start.iso_week})"

    def __str__(self) -> str:
        return f"{self.start.iso_year:04}-W{self.start.iso_week:02}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Week:
        return Week(
            moment.iso_year,
            moment.iso_week,
        )

    def __next__(self) -> CustomInterval:
        return Week.from_moment(self.stop)


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Month(CustomInterval):

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
            get_next_while(
                Day(self.start.year, self.start.month, 1),
                lambda d: d.start.month == self.start.month,
            )
        )
        # return Days(
        #     filter(
        #         lambda d: d.start.month == self.start.month,
        #         get_n_next(31, Day(self.start.year, self.start.month, 1)),
        #     )
        # )

    def day(self, day: int) -> Day:
        return Day(
            self.start.year,
            self.start.month,
            day,
        )

    def __next__(self) -> Month:
        return Month.from_moment(self.stop)


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

    def __str__(self) -> str:
        return f"{self.start.year:04}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Year:
        return Year(moment.year)

    def months(self) -> Months:
        return Months([Month(self.start.year, self.start.month + i) for i in range(12)])

    def weeks(self) -> Weeks:
        return Weeks(
            get_next_while(
                Week(self.start.year, 1),
                lambda w: w.start.iso_year == self.start.iso_year,
            )
        )

    def month(self, month: int) -> Month:
        return Month(
            self.start.year,
            month,
        )

    def __next__(self) -> Year:
        return Year.from_moment(self.stop)


class Days(Intervals[Day]):

    def months(self) -> Months:
        return Months([day.month() for day in self])


class Weeks(Intervals[Week]):
    pass


class Months(Intervals[Month]):
    pass
