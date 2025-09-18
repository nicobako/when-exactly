from __future__ import annotations

import dataclasses
from functools import cached_property
from typing import TYPE_CHECKING, Any

from when_exactly.core.custom_interval import CustomInterval
from when_exactly.core.helper_functions import gen_until as gen_until
from when_exactly.core.interval import Interval
from when_exactly.core.moment import Moment
from when_exactly.custom_collections.months import Months
from when_exactly.custom_collections.weeks import Weeks

if TYPE_CHECKING:
    from when_exactly.custom_intervals.month import Month
    from when_exactly.custom_intervals.ordinal_day import OrdinalDay
    from when_exactly.custom_intervals.week import Week
else:
    Month = Any
    Week = Any
    OrdinalDay = Any


@dataclasses.dataclass(frozen=True, init=False, repr=False)
class Year(CustomInterval):
    """The `Year` represents an entire year, starting from _January 1_ to _December 31_.

    ## Creating a Year

    ```python
    >>> import when_exactly as we

    >>> year = we.Year(2025)
    >>> year
    Year(2025)

    >>> str(year)
    '2025'

    ```

    ## The Months of a Year

    Get the [`Months`](months.md) of a year.

    ```python
    >>> months = year.months
    >>> len(months)
    12

    >>> months[0]
    Month(2025, 1)

    >>> months[-2:]
    Months([Month(2025, 11), Month(2025, 12)])

    ```

    ## The Weeks of a Year

    Get the [`Weeks`](weeks.md) of a year.

    ```python
    >>> weeks = year.weeks
    >>> len(weeks)
    52

    >>> weeks[0]
    Week(2025, 1)

    ```
    """

    def __init__(self, year: int) -> None:
        """# Create a Year.

        Parameters:
            year: The year to represent.

        Examples:
            ```python
            >>> import when_exactly as we

            >>> year = we.Year(2025)
            >>> year
            Year(2025)

            >>> str(year)
            '2025'

            ```
        """

        Interval.__init__(
            self,
            start=Moment(year, 1, 1, 0, 0, 0),
            stop=Moment(year + 1, 1, 1, 0, 0, 0),
        )

    def __repr__(self) -> str:
        return f"Year({self.start.year})"

    def __str__(self) -> str:
        return f"{self.start.year:04}"

    @classmethod
    def from_moment(cls, moment: Moment) -> Year:
        """Create a `Year` from a `Moment`."""
        return Year(moment.year)

    @cached_property
    def months(self) -> Months:
        return Months([Month(self.start.year, self.start.month + i) for i in range(12)])

    @cached_property
    def weeks(self) -> Weeks:
        return Weeks(
            gen_until(
                Week(self.start.year, 1),
                Week(self.start.year + 1, 1),
            )
        )

    def month(self, month: int) -> Month:
        """Get a specific month of the year.
        Args:
            month (int): The month number (1-12).
        """
        return Month(
            self.start.year,
            month,
        )

    @property
    def next(self) -> Year:
        return Year.from_moment(self.stop)

    def week(self, week: int) -> Week:
        return Week(
            self.start.year,
            week,
        )

    def ordinal_day(self, ordinal_day: int) -> OrdinalDay:
        return OrdinalDay(
            self.start.year,
            ordinal_day,
        )
