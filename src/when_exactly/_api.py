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
    """Represents a calendar month from the first day to the last day.

    A Month spans from 00:00:00 on the first day of the month to 00:00:00 on
    the first day of the next month (exclusive).

    Attributes:
        start: The moment at the beginning of the month (inclusive).
        stop: The moment at the beginning of the next month (exclusive).

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> month = wnx.Month(2025, 1)
        >>> month
        Month(2025, 1)
        >>> str(month)
        '2025-01'
        >>> len(list(month.days()))
        31
        >>> month.next
        Month(2025, 2)

        ```
    """

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
    """Represents an ISO 8601 week, from Monday to Sunday.

    A Week is a 7-day interval following the ISO 8601 week date system. Weeks
    are numbered from 1 to 52 (or 53 in some years). Week 1 is the first week
    containing a Thursday.

    Attributes:
        start: The moment at the beginning of Monday (inclusive).
        stop: The moment at the beginning of the next Monday (exclusive).

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> week = wnx.Week(2020, 1)
        >>> week
        Week(2020, 1)
        >>> str(week)
        '2020-W01'
        >>> week.next
        Week(2020, 2)
        >>> week.previous
        Week(2019, 52)
        >>> week.week_day(1)
        Weekday(2020, 1, 1)
        >>> len(week.week_days)
        7

        ```
    """

    def __init__(self, year: int, week: int) -> None:
        """Create a Week from ISO week year and week number.

        Args:
            year: The ISO week year.
            week: The week number (1-52 or 1-53).

        Returns:
            A Week interval.
        """
        start = Moment.from_datetime(datetime.datetime.fromisocalendar(year, week, 1))
        stop = start + Delta(days=7)
        Interval.__init__(
            self,
            start=start,
            stop=stop,
        )

    def __repr__(self) -> str:
        """Return the canonical string representation of the week."""
        return f"Week({self.start.week_year}, {self.start.week})"

    def __str__(self) -> str:
        """Return the ISO 8601 string representation of the week."""
        return f"{self.start.week_year:04}-W{self.start.week:02}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Week:
        """Create a Week from a Moment.

        Args:
            moment: The moment to extract the week from.

        Returns:
            The Week containing the moment.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2020, 1, 3, 12, 0, 0)
            >>> wnx.Week.from_moment(moment)
            Week(2020, 1)

            ```
        """
        return Week(
            moment.week_year,
            moment.week,
        )

    @property
    def next(self) -> Week:
        """The next week."""
        return Week.from_moment(self.stop)

    @property
    def previous(self) -> Week:
        """The previous week."""
        return Week.from_moment(self.start + Delta(weeks=-1))

    def week_day(self, week_day: int) -> Weekday:
        """Get a specific weekday of the week.

        Args:
            week_day: The day of week (1=Monday, 7=Sunday).

        Returns:
            The Weekday for the specified day.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> week = wnx.Week(2020, 1)
            >>> week.week_day(1)
            Weekday(2020, 1, 1)

            ```
        """
        return Weekday(
            self.start.week_year,
            self.start.week,
            week_day,
        )

    @cached_property
    def week_days(self) -> Weekdays:
        """All seven weekdays in this week."""
        return Weekdays([self.week_day(i) for i in range(1, 8)])

    @cached_property
    def days(self) -> Days:
        """All seven days in this week as Day objects."""
        return Days([self.week_day(i).to_day() for i in range(1, 8)])


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Weekday(CustomInterval):
    """Represents a single day within an ISO 8601 week.

    A Weekday is a 24-hour interval identified by its ISO week year, week number,
    and day of week (1=Monday through 7=Sunday). This is one of three day
    representations in when-exactly, alongside Day (Gregorian) and OrdinalDay.

    Attributes:
        start: The moment at midnight starting the weekday (inclusive).
        stop: The moment at midnight ending the weekday (exclusive).

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> weekday = wnx.Weekday(2020, 1, 1)
        >>> weekday
        Weekday(2020, 1, 1)
        >>> str(weekday)
        '2020-W01-1'
        >>> weekday.next
        Weekday(2020, 1, 2)
        >>> weekday.week
        Week(2020, 1)
        >>> weekday.to_day()
        Day(2019, 12, 30)

        ```
    """

    def __init__(self, year: int, week: int, week_day: int):
        """Create a Weekday from ISO week year, week number, and weekday.

        Args:
            year: The ISO week year.
            week: The week number (1-52 or 1-53).
            week_day: The day of week (1=Monday, 7=Sunday).

        Returns:
            A Weekday interval.
        """
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
        """Return the canonical string representation of the weekday."""
        return (
            f"Weekday({self.start.week_year}, {self.start.week}, {self.start.week_day})"
        )

    def __str__(self) -> str:
        """Return the ISO 8601 string representation of the weekday."""
        return f"{self.start.week_year}-W{self.start.week:02}-{self.start.week_day}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Weekday:
        """Create a Weekday from a Moment.

        Args:
            moment: The moment to extract the weekday from.

        Returns:
            The Weekday containing the moment.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2019, 12, 30, 12, 0, 0)
            >>> wnx.Weekday.from_moment(moment)
            Weekday(2020, 1, 1)

            ```
        """
        return Weekday(
            year=moment.week_year,
            week=moment.week,
            week_day=moment.week_day,
        )

    @property
    def next(self) -> Weekday:
        """The next weekday."""
        return Weekday.from_moment(moment=self.stop)

    @property
    def previous(self) -> Weekday:
        """The previous weekday."""
        return Weekday.from_moment(moment=self.start - Delta(days=1))

    @cached_property
    def week(self) -> Week:
        """The week containing this weekday."""
        return Week.from_moment(self.start)

    def to_day(self) -> Day:
        """Convert this weekday to a Day (Gregorian calendar).

        Returns:
            The corresponding Day object.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> weekday = wnx.Weekday(2020, 1, 1)
            >>> weekday.to_day()
            Day(2019, 12, 30)

            ```
        """
        return Day.from_moment(self.start)


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Day(CustomInterval):
    """Represents a single day, from midnight to midnight.

    A Day spans from 00:00:00 to 00:00:00 the next day (exclusive).

    Attributes:
        start: The moment at midnight starting the day (inclusive).
        stop: The moment at midnight ending the day (exclusive).

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> day = wnx.Day(2025, 1, 15)
        >>> day
        Day(2025, 1, 15)
        >>> str(day)
        '2025-01-15'
        >>> day.next
        Day(2025, 1, 16)
        >>> day.month
        Month(2025, 1)

        ```

    """

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
        """Get a specific hour of the day.

        Args:
            hour: The hour (0-23).

        Returns:
            The Hour for the specified hour.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> day = wnx.Day(2025, 1, 15)
            >>> day.hour(14)
            Hour(2025, 1, 15, 14)

            ```
        """
        return Hour(
            self.start.year,
            self.start.month,
            self.start.day,
            hour,
        )

    @cached_property
    def month(self) -> Month:
        """The month containing this day."""
        return Month(
            self.start.year,
            self.start.month,
        )

    @cached_property
    def week(self) -> Week:
        """The ISO week containing this day."""
        return Week.from_moment(self.start)

    @cached_property
    def ordinal_day(self) -> OrdinalDay:
        """This day as an OrdinalDay."""
        return OrdinalDay(
            self.start.year,
            self.start.ordinal_day,
        )

    @cached_property
    def weekday(self) -> Weekday:
        """This day as a Weekday."""
        return Weekday(
            self.start.year,
            self.start.week,
            self.start.week_day,
        )

    @property
    def next(self) -> Day:
        """The next day."""
        return Day.from_moment(self.stop)


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class OrdinalDay(CustomInterval):
    """Represents a single day using ordinal day-of-year numbering.

    An OrdinalDay is a 24-hour interval identified by its year and day number
    within that year (1-365 or 1-366 for leap years). This is one of three day
    representations in when-exactly, alongside Day (Gregorian) and Weekday (ISO week).

    Attributes:
        start: The moment at midnight starting the ordinal day (inclusive).
        stop: The moment at midnight ending the ordinal day (exclusive).

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> ordinal_day = wnx.OrdinalDay(2020, 1)
        >>> ordinal_day
        OrdinalDay(2020, 1)
        >>> str(ordinal_day)
        '2020-001'
        >>> ordinal_day.next
        OrdinalDay(2020, 2)
        >>> ordinal_day.previous
        OrdinalDay(2019, 365)

        ```
    """

    def __init__(self, year: int, ordinal_day: int) -> None:
        """Create an OrdinalDay from year and ordinal day number.

        Args:
            year: The year.
            ordinal_day: The day number within the year (1-365 or 1-366).

        Returns:
            An OrdinalDay interval.
        """
        start = Moment.from_datetime(
            datetime.datetime.fromordinal(
                datetime.date(year, 1, 1).toordinal() + ordinal_day - 1
            )
        )
        stop = start + Delta(days=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        """Return the canonical string representation of the ordinal day."""
        return f"OrdinalDay({self.start.year}, {self.start.ordinal_day})"

    def __str__(self) -> str:
        """Return the ordinal day string representation."""
        return f"{self.start.year:04}-{self.start.ordinal_day:03}"

    @classmethod
    def from_moment(cls, moment: Moment) -> OrdinalDay:
        """Create an OrdinalDay from a Moment.

        Args:
            moment: The moment to extract the ordinal day from.

        Returns:
            The OrdinalDay containing the moment.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2020, 1, 1, 12, 0, 0)
            >>> wnx.OrdinalDay.from_moment(moment)
            OrdinalDay(2020, 1)

            ```
        """
        return OrdinalDay(moment.year, moment.ordinal_day)

    @property
    def next(self) -> OrdinalDay:
        """The next ordinal day."""
        return OrdinalDay.from_moment(self.stop)

    @property
    def previous(self) -> OrdinalDay:
        """The previous ordinal day."""
        return OrdinalDay.from_moment(self.start - Delta(days=1))


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Hour(CustomInterval):
    """Represents a single hour, from :00 to :00 the next hour.

    An Hour is a 60-minute interval. Hours are numbered from 0 to 23.

    Attributes:
        start: The moment at the start of the hour (inclusive).
        stop: The moment at the start of the next hour (exclusive).

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> hour = wnx.Hour(2020, 1, 1, 0)
        >>> hour
        Hour(2020, 1, 1, 0)
        >>> str(hour)
        '2020-01-01T00'
        >>> hour.next
        Hour(2020, 1, 1, 1)
        >>> hour.minute(30)
        Minute(2020, 1, 1, 0, 30)
        >>> len(list(hour.minutes()))
        60

        ```
    """

    def __init__(self, year: int, month: int, day: int, hour: int) -> None:
        """Create an Hour from year, month, day, and hour.

        Args:
            year: The year.
            month: The month (1-12).
            day: The day of month.
            hour: The hour (0-23).

        Returns:
            An Hour interval.
        """
        start = Moment(year, month, day, hour, 0, 0)
        stop = start + Delta(hours=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        """Return the canonical string representation of the hour."""
        return f"Hour({self.start.year}, {self.start.month}, {self.start.day}, {self.start.hour})"

    def __str__(self) -> str:
        """Return the ISO 8601 string representation of the hour."""
        start = self.start
        return f"{start.year:04}-{start.month:02}-{start.day:02}T{start.hour:02}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Hour:
        """Create an Hour from a Moment.

        Args:
            moment: The moment to extract the hour from.

        Returns:
            The Hour containing the moment.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2020, 1, 1, 15, 30, 0)
            >>> wnx.Hour.from_moment(moment)
            Hour(2020, 1, 1, 15)

            ```
        """
        return Hour(
            moment.year,
            moment.month,
            moment.day,
            moment.hour,
        )

    def minutes(self) -> Iterable[Minute]:
        """Generate all 60 minutes in this hour.

        Returns:
            An iterable of Minute objects from :00 to :59.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> hour = wnx.Hour(2020, 1, 1, 0)
            >>> minutes = list(hour.minutes())
            >>> len(minutes)
            60
            >>> minutes[0]
            Minute(2020, 1, 1, 0, 0)

            ```
        """
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
        """Get a specific minute of the hour.

        Args:
            minute: The minute (0-59).

        Returns:
            The Minute for the specified minute.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> hour = wnx.Hour(2020, 1, 1, 0)
            >>> hour.minute(30)
            Minute(2020, 1, 1, 0, 30)

            ```
        """
        return Minute(
            self.start.year,
            self.start.month,
            self.start.day,
            self.start.hour,
            minute,
        )

    def day(self) -> Day:
        """Get the day containing this hour.

        Returns:
            The Day containing this hour.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> hour = wnx.Hour(2020, 1, 1, 0)
            >>> hour.day()
            Day(2020, 1, 1)

            ```
        """
        return Day.from_moment(self.start)

    @property
    def next(self) -> Hour:
        """The next hour."""
        return Hour.from_moment(self.stop)

    @property
    def previous(self) -> Hour:
        """The previous hour."""
        return Hour.from_moment(self.start - Delta(hours=1))


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Minute(CustomInterval):
    """Represents a single minute, from :00 to :01 the next minute.

    A Minute is a 60-second interval. Minutes are numbered from 0 to 59.

    Attributes:
        start: The moment at the start of the minute (inclusive).
        stop: The moment at the start of the next minute (exclusive).

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> minute = wnx.Minute(2020, 1, 1, 0, 0)
        >>> minute
        Minute(2020, 1, 1, 0, 0)
        >>> str(minute)
        '2020-01-01T00:00'
        >>> minute.next
        Minute(2020, 1, 1, 0, 1)
        >>> minute.second(30)
        Second(2020, 1, 1, 0, 0, 30)
        >>> len(list(minute.seconds()))
        60

        ```
    """

    def __init__(self, year: int, month: int, day: int, hour: int, minute: int) -> None:
        """Create a Minute from year, month, day, hour, and minute.

        Args:
            year: The year.
            month: The month (1-12).
            day: The day of month.
            hour: The hour (0-23).
            minute: The minute (0-59).

        Returns:
            A Minute interval.
        """
        start = Moment(year, month, day, hour, minute, 0)
        stop = start + Delta(minutes=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        """Return the canonical string representation of the minute."""
        return f"Minute({self.start.year}, {self.start.month}, {self.start.day}, {self.start.hour}, {self.start.minute})"

    def __str__(self) -> str:
        """Return the ISO 8601 string representation of the minute."""
        start = self.start
        return f"{start.year:04}-{start.month:02}-{start.day:02}T{start.hour:02}:{start.minute:02}"

    def seconds(self) -> Iterable[Second]:
        """Generate all 60 seconds in this minute.

        Returns:
            An iterable of Second objects from :00 to :59.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> minute = wnx.Minute(2020, 1, 1, 0, 0)
            >>> seconds = list(minute.seconds())
            >>> len(seconds)
            60
            >>> seconds[0]
            Second(2020, 1, 1, 0, 0, 0)

            ```
        """
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
        """Get a specific second of the minute.

        Args:
            second: The second (0-59).

        Returns:
            The Second for the specified second.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> minute = wnx.Minute(2020, 1, 1, 0, 0)
            >>> minute.second(30)
            Second(2020, 1, 1, 0, 0, 30)

            ```
        """
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
        """The next minute."""
        return Minute.from_moment(self.stop)

    @property
    def previous(self) -> Minute:
        """The previous minute."""
        return Minute.from_moment(self.start - Delta(minutes=1))

    @classmethod
    def from_moment(cls, moment: Moment) -> Minute:
        """Create a Minute from a Moment.

        Args:
            moment: The moment to extract the minute from.

        Returns:
            The Minute containing the moment.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2020, 1, 1, 15, 30, 45)
            >>> wnx.Minute.from_moment(moment)
            Minute(2020, 1, 1, 15, 30)

            ```
        """
        return Minute(
            moment.year,
            moment.month,
            moment.day,
            moment.hour,
            moment.minute,
        )


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Second(CustomInterval):
    """Represents a single second.

    A Second is a 1-second interval, the finest resolution supported by when-exactly.
    Seconds are numbered from 0 to 59.

    Attributes:
        start: The moment at the start of the second (inclusive).
        stop: The moment at the start of the next second (exclusive).

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> second = wnx.Second(2020, 1, 1, 0, 0, 0)
        >>> second
        Second(2020, 1, 1, 0, 0, 0)
        >>> str(second)
        '2020-01-01T00:00:00'
        >>> second.next
        Second(2020, 1, 1, 0, 0, 1)
        >>> second.minute()
        Minute(2020, 1, 1, 0, 0)

        ```
    """

    def __init__(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int
    ) -> None:
        """Create a Second from year, month, day, hour, minute, and second.

        Args:
            year: The year.
            month: The month (1-12).
            day: The day of month.
            hour: The hour (0-23).
            minute: The minute (0-59).
            second: The second (0-59).

        Returns:
            A Second interval.
        """
        start = Moment(year, month, day, hour, minute, second)
        stop = start + Delta(seconds=1)
        Interval.__init__(self, start=start, stop=stop)

    def __repr__(self) -> str:
        """Return the canonical string representation of the second."""
        return f"Second({self.start.year}, {self.start.month}, {self.start.day}, {self.start.hour}, {self.start.minute}, {self.start.second})"

    def __str__(self) -> str:
        """Return the ISO 8601 string representation of the second."""
        start = self.start
        return f"{start.year:04}-{start.month:02}-{start.day:02}T{start.hour:02}:{start.minute:02}:{start.second:02}"

    def minute(self) -> Minute:
        """Get the minute containing this second.

        Returns:
            The Minute containing this second.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> second = wnx.Second(2020, 1, 1, 0, 0, 30)
            >>> second.minute()
            Minute(2020, 1, 1, 0, 0)

            ```
        """
        return Minute.from_moment(self.start)

    @property
    def next(self) -> Second:
        """The next second."""
        return Second.from_moment(self.stop)

    @property
    def previous(self) -> Second:
        """The previous second."""
        return Second.from_moment(self.start - Delta(seconds=1))

    @classmethod
    def from_moment(cls, moment: Moment) -> Second:
        """Create a Second from a Moment.

        Args:
            moment: The moment to extract the second from.

        Returns:
            The Second containing the moment.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2020, 1, 1, 15, 30, 45)
            >>> wnx.Second.from_moment(moment)
            Second(2020, 1, 1, 15, 30, 45)

            ```
        """
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
    """A collection of Year intervals.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> years = wnx.Years([wnx.Year(2024), wnx.Year(2025), wnx.Year(2023)])
        >>> len(years)
        3
        >>> years[0]  # Sorted automatically
        Year(2023)

        ```
    """

    pass


class Weeks(CustomCollection[Week]):
    """A collection of Week intervals.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> weeks = wnx.Weeks([wnx.Week(2025, 1), wnx.Week(2025, 2)])
        >>> len(weeks)
        2

        ```
    """

    pass


class Weekdays(CustomCollection[Weekday]):
    """A collection of Weekday intervals.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> weekdays = wnx.Weekdays([
        ...     wnx.Weekday(2020, 1, 1),
        ...     wnx.Weekday(2020, 1, 3),
        ... ])
        >>> len(weekdays)
        2
        >>> weekdays[0]
        Weekday(2020, 1, 1)

        ```
    """

    pass


class Months(CustomCollection[Month]):
    """A collection of Month intervals.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> months = wnx.Months([wnx.Month(2025, 1), wnx.Month(2025, 3)])
        >>> len(months)
        2
        >>> months[0]
        Month(2025, 1)

        ```
    """

    pass


class Days(CustomCollection[Day]):
    """A collection of Day intervals.

    Days provides additional functionality beyond the base Collection, including
    the ability to get all unique months that the days span.

    Attributes:
        months: All unique months that the days in this collection span.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> days = wnx.Days([
        ...     wnx.Day(2025, 1, 1),
        ...     wnx.Day(2025, 1, 15),
        ...     wnx.Day(2025, 2, 1),
        ... ])
        >>> len(days)
        3
        >>> days.months
        Months([Month(2025, 1), Month(2025, 2)])

        ```
    """

    @cached_property
    def months(self) -> Months:
        return Months([day.month for day in self.values])


class Hours(CustomCollection[Hour]):
    """A collection of Hour intervals.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> hours = wnx.Hours([
        ...     wnx.Hour(2020, 1, 1, 0),
        ...     wnx.Hour(2020, 1, 1, 12),
        ... ])
        >>> len(hours)
        2
        >>> hours[0]
        Hour(2020, 1, 1, 0)

        ```
    """

    pass


class Minutes(CustomCollection[Minute]):
    """A collection of Minute intervals.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> minutes = wnx.Minutes([
        ...     wnx.Minute(2020, 1, 1, 0, 0),
        ...     wnx.Minute(2020, 1, 1, 0, 30),
        ... ])
        >>> len(minutes)
        2
        >>> minutes[0]
        Minute(2020, 1, 1, 0, 0)

        ```
    """

    pass


class Seconds(CustomCollection[Second]):
    """A collection of Second intervals.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> seconds = wnx.Seconds([
        ...     wnx.Second(2020, 1, 1, 0, 0, 0),
        ...     wnx.Second(2020, 1, 1, 0, 0, 30),
        ... ])
        >>> len(seconds)
        2
        >>> seconds[0]
        Second(2020, 1, 1, 0, 0, 0)

        ```
    """

    pass


# endregion Custom Collections
