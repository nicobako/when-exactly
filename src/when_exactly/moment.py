from __future__ import annotations

import dataclasses
import datetime

from when_exactly.delta import Delta
from when_exactly.errors import InvalidMomentError


@dataclasses.dataclass(frozen=True)
class Moment:
    """A Moment represents a specific point in time with year, month, day, hour, minute, and second.

    The `Moment` is analogous to the builtin [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) class,
    but it is immutable and provides additional functionality for date arithmetic."""

    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def to_datetime(self) -> datetime.datetime:
        return datetime.datetime(
            self.year, self.month, self.day, self.hour, self.minute, self.second
        )

    @classmethod
    def from_datetime(cls, dt: datetime.datetime) -> Moment:
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
        ):  # if the day is too large for the month, we need to decrement it until it is valid
            try:
                Moment(**new_moment_kwargs)  # type: ignore
                break
            except ValueError:
                new_moment_kwargs["day"] -= 1

        dt = Moment(**new_moment_kwargs).to_datetime()  # type: ignore

        dt += datetime.timedelta(weeks=delta.weeks)
        dt += datetime.timedelta(days=delta.days)
        dt += datetime.timedelta(hours=delta.hours)
        dt += datetime.timedelta(minutes=delta.minutes)
        dt += datetime.timedelta(seconds=delta.seconds)

        return Moment.from_datetime(dt)

    def __sub__(self, delta: Delta) -> Moment:
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
        return self.to_datetime().isocalendar()[0]

    @property
    def week(self) -> int:
        return self.to_datetime().isocalendar()[1]

    @property
    def week_day(self) -> int:
        return self.to_datetime().isocalendar()[2]

    @property
    def ordinal_day(self) -> int:
        return (
            self.to_datetime().toordinal()
            - datetime.date(self.year, 1, 1).toordinal()
            + 1
        )
