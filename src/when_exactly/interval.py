from __future__ import annotations

import dataclasses
from typing import Iterable

from when_exactly.moment import Moment


@dataclasses.dataclass(frozen=True)
class Interval:
    start: Moment
    stop: Moment

    def months(self) -> Iterable[Interval]:
        start = self.start
        next_start = start.next_month()
        while next_start <= self.stop:
            yield Interval(start, next_start)
            start = next_start
            next_start = start.next_month()

    def __post_init__(self) -> None:
        if self.start >= self.stop:
            raise ValueError("Interval start must be before stop")
