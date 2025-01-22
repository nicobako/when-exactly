from __future__ import annotations

import dataclasses
from typing import Iterable

from when_exactly.moment import Moment


@dataclasses.dataclass(frozen=True)
class Interval:
    start: Moment
    stop: Moment
