from __future__ import annotations

import dataclasses
import datetime

from when_exactly.delta import Delta


@dataclasses.dataclass(frozen=True)
class Moment:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"

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
            raise ValueError(f"Invalid moment: {e}") from e

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
                Moment(**new_moment_kwargs)
                break
            except ValueError:
                new_moment_kwargs["day"] -= 1

        dt = Moment(**new_moment_kwargs).to_datetime()

        dt += datetime.timedelta(weeks=delta.weeks)
        dt += datetime.timedelta(days=delta.days)
        dt += datetime.timedelta(hours=delta.hours)
        dt += datetime.timedelta(minutes=delta.minutes)
        dt += datetime.timedelta(seconds=delta.seconds)

        return Moment.from_datetime(dt)
