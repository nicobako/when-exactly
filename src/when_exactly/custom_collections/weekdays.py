from __future__ import annotations

from typing import TYPE_CHECKING, Any

from when_exactly.core.custom_collection import CustomCollection

if TYPE_CHECKING:
    from when_exactly.custom_intervals.weekday import Weekday
else:
    Weekday = Any


class Weekdays(CustomCollection[Weekday]):
    pass
