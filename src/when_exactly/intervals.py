from __future__ import annotations

from typing import Iterable, NoReturn, TypeVar, final, overload

from when_exactly.core.interval import Interval

T = TypeVar("T", bound=Interval)

from collections import abc


class Intervals(abc.Container[T]):
    @final
    def __init__(self, values: Iterable[T]) -> None:
        self._values: list[T] = sorted(set(values))
        self._counter = 0

    @property
    def values(self) -> list[T]:
        return self._values

    @final
    def __iter__(self) -> Intervals[T]:
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
    def __getitem__(self, index: slice[int]) -> Intervals[T]: ...

    @final
    def __getitem__(self, index: int | slice[int]) -> T | Intervals[T]:
        if isinstance(index, slice):
            return Intervals(self._values[index])
        else:
            return self._values[index]

    @final
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._values})"

    @overload
    def __eq__(self, other: Intervals[T]) -> bool: ...

    @overload
    def __eq__(self, other: object) -> bool: ...

    @final
    def __eq__(self, other: Intervals[T] | object) -> bool:
        if not isinstance(other, Intervals):
            raise NotImplementedError

        return self._values == other.values

    def __reversed__(self) -> NoReturn:
        raise NotImplementedError

    @final
    def __len__(self) -> int:
        return len(self._values)

    def __str__(self) -> str:
        return "{" + ", ".join(str(value) for value in self._values) + "}"
