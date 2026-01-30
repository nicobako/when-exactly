from __future__ import annotations

from typing import Iterable, NoReturn, final, overload

from when_exactly.core.interval import Interval


class Collection[T: Interval]:
    """A Collection is an ordered, deduplicated set of Intervals.

    Collections automatically sort their values and remove duplicates. They provide
    iteration, indexing, slicing, and membership testing operations. Collections are
    the base class for concrete types like Days, Months, Years, etc.

    Type Parameters:
        T: The type of Interval this collection holds.

    Attributes:
        values: A sorted list of unique intervals in this collection.

    Example:
        ```python
        >>> import when_exactly as wnx
        >>> # Days is a subclass of Collection
        >>> days = wnx.Days([
        ...     wnx.Day(2025, 1, 1),
        ...     wnx.Day(2025, 1, 3),
        ...     wnx.Day(2025, 1, 2),
        ...     wnx.Day(2025, 1, 1),  # duplicate, will be removed
        ... ])
        >>> len(days)
        3
        >>> days[0]
        Day(2025, 1, 1)
        >>> wnx.Day(2025, 1, 2) in days
        True

        ```
    """
    @final
    def __init__(self, values: Iterable[T]) -> None:
        """Initialize a Collection with the given intervals.

        Args:
            values: An iterable of intervals. Duplicates will be removed and
                    the intervals will be sorted.
        """
        self._values: list[T] = sorted(set(values))
        self._counter = 0

    @property
    def values(self) -> list[T]:
        """Get the sorted list of unique intervals in this collection.

        Returns:
            A sorted list of intervals.
        """
        return self._values

    @final
    def __iter__(self) -> Collection[T]:
        return self

    @final
    def __next__(self) -> T:
        try:
            value = self._values[self._counter]
            self._counter += 1
            return value
        except IndexError:
            self._counter = 0
            raise StopIteration

    @final
    def __contains__(self, x: object) -> bool:
        return self._values.__contains__(x)

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(
        self, index: slice[int, int | None, int | None]
    ) -> Collection[T]: ...

    @final
    def __getitem__(
        self, index: int | slice[int, int | None, int | None]
    ) -> T | Collection[T]:
        if isinstance(index, slice):
            return self.__class__(self._values[index])
        else:
            return self._values[index]

    @final
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._values})"

    @overload
    def __eq__(self, other: Collection[T]) -> bool: ...

    @overload
    def __eq__(self, other: object) -> bool: ...

    @final
    def __eq__(self, other: Collection[T] | object) -> bool:
        if not isinstance(other, Collection):
            raise NotImplementedError

        if not isinstance(other, self.__class__):
            return False

        return self._values == other.values

    def __reversed__(self) -> NoReturn:
        raise NotImplementedError

    @final
    def __len__(self) -> int:
        return len(self._values)

    def __str__(self) -> str:
        return "{" + ", ".join(str(value) for value in self._values) + "}"
