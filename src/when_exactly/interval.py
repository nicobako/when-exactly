from __future__ import annotations

import dataclasses

from when_exactly.moment import Moment


@dataclasses.dataclass(frozen=True)
class Interval:
    start: Moment
    stop: Moment

    def __post_init__(self) -> None:
        if self.start >= self.stop:
            raise ValueError("Interval start must be before stop")

    def __next__(self) -> Interval:
        raise NotImplementedError
