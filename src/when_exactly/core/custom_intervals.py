from typing import Generic, TypeVar

from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.intervals import Intervals

CustomIntervalType = TypeVar("CustomIntervalType", bound=CustomInterval)


class CustomIntervals(Generic[CustomIntervalType], Intervals[CustomIntervalType]):
    pass
