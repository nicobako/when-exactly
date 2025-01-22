from __future__ import annotations

import dataclasses
from typing import Iterable

from when_exactly.delta import Delta
from when_exactly.moment import Moment


@dataclasses.dataclass(frozen=True)
class Interval:
    start: Moment
    stop: Moment

    def __post_init__(self) -> None:
        if self.start >= self.stop:
            raise ValueError("Interval start must be before stop")

    def __add__(self, delta: Delta) -> Interval:
        return Interval(
            self.start + delta,
            self.stop + delta,
        )
