from __future__ import annotations
import dataclasses
from typing import Iterable

from when_exactly.moment import Moment

@dataclasses.dataclass(frozen=True)
class Interval:
    start: Moment
    stop: Moment

    def days(self) -> Iterable[Interval]:
        current = self.start
        while current < self.stop:
            next_day = current.add(days=1)
            yield Interval(current, next_day)
            current = next_day