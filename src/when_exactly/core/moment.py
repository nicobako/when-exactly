from __future__ import annotations

import dataclasses
import datetime

from when_exactly.core.delta import Delta
from when_exactly.core.errors import InvalidMomentError


@dataclasses.dataclass(frozen=True)
class Moment:
    """A Moment represents a specific point in time with year, month, day, hour, minute, and second.

    The `Moment` is analogous to the builtin [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) class,
    but it is immutable and provides additional functionality for date arithmetic.

    Attributes:
        year: The year (e.g., 2025)
        month: The month (1-12)
        day: The day of the month (1-31)
        hour: The hour (0-23)
        minute: The minute (0-59)
        second: The second (0-59)

    Raises:
        InvalidMomentError: If the provided values don't represent a valid date/time.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> moment = wnx.Moment(2025, 1, 30, 15, 25, 30)
        >>> moment
        Moment(year=2025, month=1, day=30, hour=15, minute=25, second=30)
        >>> moment.year
        2025
        >>> moment + wnx.Delta(days=1)
        Moment(year=2025, month=1, day=31, hour=15, minute=25, second=30)

        ```

    """

    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def to_datetime(self) -> datetime.datetime:
        """Convert this Moment to a Python datetime.datetime object.

        Returns:
            A datetime.datetime object representing the same point in time.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2025, 1, 30, 15, 25, 30)
            >>> moment.to_datetime()
            datetime.datetime(2025, 1, 30, 15, 25, 30)

            ```
        """
        return datetime.datetime(
            self.year, self.month, self.day, self.hour, self.minute, self.second
        )

    @classmethod
    def from_datetime(cls, dt: datetime.datetime) -> Moment:
        """Create a Moment from a Python datetime.datetime object.

        Args:
            dt: The datetime object to convert.

        Returns:
            A new Moment representing the same point in time.

        Example:
            ```python
            >>> import datetime
            >>> import when_exactly as wnx
            >>> dt = datetime.datetime(2025, 1, 30, 15, 25, 30)
            >>> wnx.Moment.from_datetime(dt)
            Moment(year=2025, month=1, day=30, hour=15, minute=25, second=30)

            ```
        """
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    def __post_init__(self) -> None:
        try:
            self.to_datetime()
        except ValueError as e:
            raise InvalidMomentError(str(e)) from e

    def __lt__(self, other: Moment) -> bool:
        return self.to_datetime() < other.to_datetime()

    def __le__(self, other: Moment) -> bool:
        return self.to_datetime() <= other.to_datetime()

    def __add__(self, delta: Delta) -> Moment:
        """Add a Delta to this Moment to get a new Moment.

        Args:
            delta: The time delta to add.

        Returns:
            A new Moment representing the point in time after adding the delta.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2025, 1, 31, 12, 30, 30)
            >>> moment + wnx.Delta(days=2)
            Moment(year=2025, month=2, day=2, hour=12, minute=30, second=30)
            >>> moment + wnx.Delta(months=1)
            Moment(year=2025, month=2, day=28, hour=12, minute=30, second=30)

            ```
        """
        new_moment_kwargs = {
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "hour": self.hour,
            "minute": self.minute,
            "second": self.second,
        }
        if delta.years != 0:
            new_moment_kwargs["year"] += delta.years

        if delta.months != 0:
            new_moment_kwargs["month"] += delta.months
            while new_moment_kwargs["month"] > 12:
                new_moment_kwargs["month"] -= 12
                new_moment_kwargs["year"] += 1

            while new_moment_kwargs["month"] < 1:
                new_moment_kwargs["month"] += 12
                new_moment_kwargs["year"] -= 1

        while (
            new_moment_kwargs["day"] > 28
        ):  # if the day is too large for the month, wnx need to decrement it until it is valid
            try:
                Moment(**new_moment_kwargs)  # type: ignore
                break
            except InvalidMomentError:
                new_moment_kwargs["day"] -= 1

        dt = Moment(**new_moment_kwargs).to_datetime()  # type: ignore

        dt += datetime.timedelta(weeks=delta.weeks)
        dt += datetime.timedelta(days=delta.days)
        dt += datetime.timedelta(hours=delta.hours)
        dt += datetime.timedelta(minutes=delta.minutes)
        dt += datetime.timedelta(seconds=delta.seconds)

        return Moment.from_datetime(dt)

    def __sub__(self, delta: Delta) -> Moment:
        """Subtract a Delta from this Moment to get a new Moment.

        Args:
            delta: The time delta to subtract.

        Returns:
            A new Moment representing the point in time after subtracting the delta.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2025, 2, 5, 12, 30, 30)
            >>> moment - wnx.Delta(days=5)
            Moment(year=2025, month=1, day=31, hour=12, minute=30, second=30)

            ```
        """
        return self + Delta(
            years=-delta.years,
            months=-delta.months,
            weeks=-delta.weeks,
            days=-delta.days,
            hours=-delta.hours,
            minutes=-delta.minutes,
            seconds=-delta.seconds,
        )

    def __str__(self) -> str:
        return self.to_datetime().isoformat()

    @property
    def week_year(self) -> int:
        """The ISO week-numbering year of this moment.

        Returns:
            The ISO year, which may differ from the calendar year.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> # December 31, 2019 is in ISO week 2020-W01
            >>> moment = wnx.Moment(2019, 12, 31, 0, 0, 0)
            >>> moment.week_year
            2020

            ```
        """
        return self.to_datetime().isocalendar()[0]

    @property
    def week(self) -> int:
        """The ISO week number of this moment (1-53).

        Returns:
            The ISO week number.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2020, 1, 1, 0, 0, 0)
            >>> moment.week
            1

            ```
        """
        return self.to_datetime().isocalendar()[1]

    @property
    def week_day(self) -> int:
        """The ISO weekday of this moment (1=Monday, 7=Sunday).

        Returns:
            The ISO weekday number.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> # January 1, 2020 was a Wednesday
            >>> moment = wnx.Moment(2020, 1, 1, 0, 0, 0)
            >>> moment.week_day
            3

            ```
        """
        return self.to_datetime().isocalendar()[2]

    @property
    def ordinal_day(self) -> int:
        """The day of the year (1-366).

        Returns:
            The ordinal day within the year.

        Example:
            ```python
            >>> import when_exactly as wnx
            >>> moment = wnx.Moment(2020, 1, 1, 0, 0, 0)
            >>> moment.ordinal_day
            1
            >>> moment = wnx.Moment(2020, 12, 31, 0, 0, 0)
            >>> moment.ordinal_day
            366

            ```
        """
        return (
            self.to_datetime().toordinal()
            - datetime.date(self.year, 1, 1).toordinal()
            + 1
        )
