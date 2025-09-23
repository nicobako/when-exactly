import pytest

import when_exactly as wnx


@pytest.fixture  # type: ignore
def values() -> list[wnx.Interval]:
    return [
        wnx.Interval(wnx.Moment(2020, 1, 1, 0, 0, 0), wnx.Moment(2020, 1, 2, 0, 0, 0)),
        wnx.Interval(wnx.Moment(2020, 1, 2, 0, 0, 0), wnx.Moment(2020, 1, 3, 0, 0, 0)),
        wnx.Interval(wnx.Moment(2020, 1, 3, 0, 0, 0), wnx.Moment(2020, 1, 4, 0, 0, 0)),
    ]


@pytest.fixture  # type: ignore
def intervals(values: list[wnx.Interval]) -> wnx.Collection[wnx.Interval]:
    return wnx.Collection(values)


def test_collection_api(
    values: list[wnx.Interval], intervals: wnx.Collection[wnx.Interval]
) -> None:
    assert list(intervals) == values
    assert list(intervals) == values

    assert values[0] in intervals
    assert intervals[0] == values[0]

    assert intervals[0:2] == wnx.Collection(values[0:2])
    assert intervals == intervals

    with pytest.raises(NotImplementedError):
        assert reversed(intervals)

    assert len(intervals) == 3


def test_collection_sorts_and_removes_duplicates() -> None:
    a = wnx.Interval(wnx.Moment(2020, 1, 1, 0, 0, 0), wnx.Moment(2020, 1, 2, 0, 0, 0))
    b = wnx.Interval(wnx.Moment(2020, 1, 2, 0, 0, 0), wnx.Moment(2020, 1, 3, 0, 0, 0))
    c = wnx.Interval(wnx.Moment(2020, 1, 3, 0, 0, 0), wnx.Moment(2020, 1, 4, 0, 0, 0))

    values = [a, b, c, a, b, c]
    intervals = wnx.Collection(values)
    assert list(intervals) == [a, b, c]
