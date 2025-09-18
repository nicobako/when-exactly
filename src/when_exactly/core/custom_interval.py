from __future__ import annotations

import dataclasses
from copy import deepcopy
from typing import Any

from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class CustomInterval(Interval):
    """A custom intervval.

    This class serves as a base class from which custom intervals can be derived.
    It provides the necessary interface and methods to be implemented by subclasses.

    """

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
