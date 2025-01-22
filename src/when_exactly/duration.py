from __future__ import annotations
import dataclasses
@dataclasses.dataclass(kw_only=True, frozen=True)
class Duration:
    years: int = 0
    months: int = 0
    weeks: int = 0
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0

    def __add__(self, other: Duration) -> Duration:
        return Duration(
            years=self.years + other.years,
            months=self.months + other.months,
            weeks=self.weeks + other.weeks,
            days=self.days + other.days,
            hours=self.hours + other.hours,
            minutes=self.minutes + other.minutes,
            seconds=self.seconds + other.seconds,
        )