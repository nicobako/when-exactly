from __future__ import annotations

import dataclasses

from when_exactly.core.moment import Moment


@dataclasses.dataclass(frozen=True)
class Interval:
    """An Interval represents a continuous span of time between two moments.

    An Interval is defined by a start moment (inclusive) and a stop moment (exclusive),
    following the half-open interval convention [start, stop). The start must always
    be before the stop.

    Attributes:
        start: The beginning moment of the interval (inclusive).
        stop: The ending moment of the interval (exclusive).

    Raises:
        ValueError: If start is not before stop.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> start = wnx.Moment(2025, 1, 1, 0, 0, 0)
        >>> stop = wnx.Moment(2025, 1, 2, 0, 0, 0)
        >>> interval = wnx.Interval(start=start, stop=stop)
        >>> interval
        Interval(start=Moment(year=2025, month=1, day=1, hour=0, minute=0, second=0), stop=Moment(year=2025, month=1, day=2, hour=0, minute=0, second=0))

        >>> # String representation uses ISO 8601 interval notation
        >>> str(interval)
        '2025-01-01T00:00:00/2025-01-02T00:00:00'

        ```
    """
    start: Moment
    stop: Moment

    def __post_init__(self) -> None:
        if self.start >= self.stop:
            raise ValueError("Interval start must be before stop")

    def __lt__(self, other: Interval) -> bool:
        return self.start < other.start or self.stop < other.stop

    def __le__(self, other: Interval) -> bool:
        return self.start <= other.start or self.stop <= other.stop

    def __str__(self) -> str:
        return f"{self.start}/{self.stop}"
