from __future__ import annotations

from typing import Generic, Iterable, TypeVar

from when_exactly.interval import Interval

T = TypeVar("T", bound=Interval)

from collections import abc


class Intervals(abc.Iterable[T], Generic[T]):
    def __init__(self, values: Iterable[T]) -> None:
        self._values = list(values)
        self._counter = 0

    def __iter__(self) -> Intervals[T]:
        return self

    def __next__(self) -> T:
        try:
            value = self._values[self._counter]
            return value
        except IndexError:
            raise StopIteration
