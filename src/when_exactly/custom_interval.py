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
    precision: Precision

    def __init__(self, precision: Precision, *args: Any, **kwargs: Any) -> None:
        Interval.__init__(self, *args, **kwargs)
        object.__setattr__(self, "precision", precision)

    @classmethod
    def from_moment(cls, moment: Moment) -> CustomInterval[P]:
        raise NotImplementedError("CustomInterval from_moment not implemented")

    @property
    def next(self) -> CustomInterval[P]:
        raise NotImplementedError("CustomInterval next not implemented")

    @property
    def previous(self) -> CustomInterval[P]:
        raise NotImplementedError("CustomInterval previous not implemented")

    def __repr__(self) -> str:
        raise NotImplementedError("CustomInterval repr not implemented")

    def __str__(self) -> str:
        raise NotImplementedError("CustomInterval str not implemented")

    def __add__(self, value: int) -> CustomInterval[P]:
        next_value = deepcopy(self)
        for _ in range(value):
            next_value = next_value.next
        return next_value

    def __sub__(self, value: int) -> CustomInterval[P]:
        prev_value = deepcopy(self)
        for _ in range(value):
            prev_value = prev_value.previous
        return prev_value
