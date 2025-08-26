from __future__ import annotations

import dataclasses
import datetime
from copy import deepcopy
from enum import Enum
from typing import Any, Self

from when_exactly.delta import Delta
from when_exactly.interval import Interval
from when_exactly.moment import Moment
from when_exactly.precision import Precision


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class CustomInterval(Interval):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        Interval.__init__(self, *args, **kwargs)

    @classmethod
    def from_moment(cls, moment: Moment) -> CustomInterval:
        raise NotImplementedError("CustomInterval from_moment not implemented")

    @property
    def next(self) -> CustomInterval:
        raise NotImplementedError("CustomInterval next not implemented")

    @property
    def previous(self) -> CustomInterval:
        raise NotImplementedError("CustomInterval previous not implemented")

    @property
    def precision(self) -> Precision:
        raise NotImplementedError("CustomInterval precision not implemented")

    def __repr__(self) -> str:
        raise NotImplementedError("CustomInterval repr not implemented")

    def __str__(self) -> str:
        raise NotImplementedError("CustomInterval str not implemented")

    def __add__(self, value: int) -> CustomInterval:
        next_value = deepcopy(self)
        for _ in range(value):
            next_value = next_value.next
        return next_value

    def __sub__(self, value: int) -> CustomInterval:
        prev_value = deepcopy(self)
        for _ in range(value):
            prev_value = prev_value.previous
        return prev_value
