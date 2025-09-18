from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any

from when_exactly.core.custom_collection import CustomCollection

if TYPE_CHECKING:
    from when_exactly.custom_collections.months import Months
    from when_exactly.custom_intervals.day import Day
else:
    Day = Any
    Months = Any


class Days(CustomCollection[Day]):
    @cached_property
    def months(self) -> Months:
        return Months([day.month for day in self.values])
