from __future__ import annotations

import dataclasses

from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class CustomInterval(Interval):
    def __init__(self, *args: int, **kwargs: int):
        raise NotImplementedError(
            "CustomInterval init not implemented"
        )  # pragma: no cover

    def __repr__(self) -> str:
        raise NotImplementedError(
            "CustomInterval repr not implemented"
        )  # pragma: no cover

    @classmethod
    def from_moment(cls, moment: Moment) -> CustomInterval:
        raise NotImplementedError(
            "CustomInterval from_moment not implemented"
        )  # pragma: no cover

    def __next__(self) -> CustomInterval:
        raise NotImplementedError(
            "CustomInterval next not implemented"
        )  # pragma: no cover

    def __str__(self) -> str:
        raise NotImplementedError(
            "CustomInterval str not implemented"
        )  # pragma: no cover
