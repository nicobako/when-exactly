from __future__ import annotations

from typing import Iterable

from when_exactly.core.custom_interval import CustomInterval


def gen_until[I: CustomInterval](start: I, stop: I) -> Iterable[I]:
    while start < stop:
        yield start
        start = start.next  # type: ignore
