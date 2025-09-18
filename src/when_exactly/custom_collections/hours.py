from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from when_exactly.custom_intervals.hour import Hour
else:
    Hour = Any
from when_exactly.core.custom_collection import CustomCollection


class Hours(CustomCollection[Hour]):
    pass
