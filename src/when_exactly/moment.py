from __future__ import annotations

import dataclasses
import datetime


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