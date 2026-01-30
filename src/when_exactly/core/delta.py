from __future__ import annotations

import dataclasses


@dataclasses.dataclass(kw_only=True, frozen=True)
class Delta:
    """A Delta represents a duration of time that can be added to or subtracted from a Moment.

    Unlike Python's `timedelta`, Delta supports month and year arithmetic, which is essential
    for calendar-aware date operations. All attributes default to 0 and must be specified
    as keyword arguments.

    Attributes:
        years: Number of years in the delta.
        months: Number of months in the delta.
        weeks: Number of weeks in the delta.
        days: Number of days in the delta.
        hours: Number of hours in the delta.
        minutes: Number of minutes in the delta.
        seconds: Number of seconds in the delta.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> # Create various deltas
        >>> delta = wnx.Delta(days=5, hours=3)
        >>> delta
        Delta(years=0, months=0, weeks=0, days=5, hours=3, minutes=0, seconds=0)

        >>> # Add to a moment
        >>> moment = wnx.Moment(2025, 1, 15, 10, 0, 0)
        >>> moment + wnx.Delta(months=1, days=10)
        Moment(year=2025, month=2, day=25, hour=10, minute=0, second=0)

        >>> # Handle month-end edge cases
        >>> wnx.Moment(2025, 1, 31, 0, 0, 0) + wnx.Delta(months=1)
        Moment(year=2025, month=2, day=28, hour=0, minute=0, second=0)

        ```
    """
    years: int = 0
    months: int = 0
    weeks: int = 0
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
