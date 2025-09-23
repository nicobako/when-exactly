"""All public API objects.

This module is created to avoid circular imports.
Nearly all public API objects depend on each other,
so putting them all in one single module helps prevent circular imports.
"""

from __future__ import annotations

import dataclasses
import datetime
from functools import cached_property
from typing import Iterable

from when_exactly.core.custom_collection import CustomCollection
from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.delta import Delta
from when_exactly.core.helper_functions import gen_until
from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment

# region Custom Intervals


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Year(CustomInterval):
    """The `Year` represents an entire year, starting from _January 1_ to _December 31_.

    ## Creating a Year

    ```python
    >>> import when_exactly as wnx

    >>> year = wnx.Year(2025)
    >>> year
    Year(2025)

    >>> str(year)
    '2025'

    ```

    ## The Months of a Year

    Get the [`Months`](months.md) of a year.

    ```python
    >>> months = year.months
    >>> len(months)
    12

    >>> months[0]
    Month(2025, 1)

    >>> months[-2:]
    Months([Month(2025, 11), Month(2025, 12)])

    ```

    ## The Weeks of a Year

    Get the [`Weeks`](weeks.md) of a year.

    ```python
    >>> weeks = year.weeks
    >>> len(weeks)
    52

    >>> weeks[0]
    Week(2025, 1)

    ```
    """

    def __init__(self, year: int) -> None:
        """# Create a Year.

        Parameters:
            year: The year to represent.

        Examples:
            ```python
            >>> import when_exactly as wnx

            >>> year = wnx.Year(2025)
            >>> year
            Year(2025)

            >>> str(year)
            '2025'

            ```
        """

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
        """Create a `Year` from a `Moment`."""
        return Year(moment.year)

    @cached_property
    def months(self) -> Months:
        return Months([Month(self.start.year, self.start.month + i) for i in range(12)])

    @cached_property
    def weeks(self) -> Weeks:
        return Weeks(
            gen_until(
                Week(self.start.year, 1),
                Week(self.start.year + 1, 1),
            )
        )

    def month(self, month: int) -> Month:
        """Get a specific month of the year.
        Args:
            month (int): The month number (1-12).
        """
        return Month(
            self.start.year,
            month,
        )

    @property
    def next(self) -> Year:
        return Year.from_moment(self.stop)

    @property
    def previous(self) -> Year:
        return Year(self.start.year - 1)

    def week(self, week: int) -> Week:
        return Week(
            self.start.year,
            week,
        )

    def ordinal_day(self, ordinal_day: int) -> OrdinalDay:
        return OrdinalDay(
            self.start.year,
            ordinal_day,
        )


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

    @property
    def previous(self) -> Month:
        return Month.from_moment(self.start + Delta(months=-1))


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

    @property
    def previous(self) -> Week:
        return Week.from_moment(self.start + Delta(weeks=-1))

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

    @property
    def previous(self) -> Weekday:
        return Weekday.from_moment(moment=self.start - Delta(days=1))

    @cached_property
    def week(self) -> Week:
        return Week.from_moment(self.start)

    def to_day(self) -> Day:
        return Day.from_moment(self.start)


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

    @property
    def previous(self) -> OrdinalDay:
        return OrdinalDay.from_moment(self.start - Delta(days=1))


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
            minute = minute.next

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

    @property
    def next(self) -> Hour:
        return Hour.from_moment(self.stop)

    @property
    def previous(self) -> Hour:
        return Hour.from_moment(self.start - Delta(hours=1))


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
            second = second.next

    def second(self, second: int) -> Second:
        return Second(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            self.start.minute,
            second,
        )

    @property
    def next(self) -> Minute:
        return Minute.from_moment(self.stop)

    @property
    def previous(self) -> Minute:
        return Minute.from_moment(self.start - Delta(minutes=1))

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

    @property
    def previous(self) -> Second:
        return Second.from_moment(self.start - Delta(seconds=1))

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


# endregion Custom Intervals


# region Custom Collections
class Years(CustomCollection[Year]):
    pass


class Weeks(CustomCollection[Week]):
    pass


class Weekdays(CustomCollection[Weekday]):
    pass


class Months(CustomCollection[Month]):
    pass


class Days(CustomCollection[Day]):
    @cached_property
    def months(self) -> Months:
        return Months([day.month for day in self.values])


class Hours(CustomCollection[Hour]):
    pass


class Minutes(CustomCollection[Minute]):
    pass


class Seconds(CustomCollection[Second]):
    pass


# endregion Custom Collections
