import pytest

import when_exactly as we


@pytest.fixture  # type: ignore
def values() -> list[we.Interval]:
    return [
        we.Interval(we.Moment(2020, 1, 1, 0, 0, 0), we.Moment(2020, 1, 2, 0, 0, 0)),
        we.Interval(we.Moment(2020, 1, 2, 0, 0, 0), we.Moment(2020, 1, 3, 0, 0, 0)),
        we.Interval(we.Moment(2020, 1, 3, 0, 0, 0), we.Moment(2020, 1, 4, 0, 0, 0)),
    ]


@pytest.fixture  # type: ignore
def intervals(values: list[we.Interval]) -> we.Collection[we.Interval]:
    return we.Collection(values)


def test_collection_api(
    values: list[we.Interval], intervals: we.Collection[we.Interval]
) -> None:
    assert list(intervals) == values
    assert list(intervals) == values

    assert values[0] in intervals
    assert intervals[0] == values[0]

    assert intervals[0:2] == we.Collection(values[0:2])
    assert intervals == intervals

    with pytest.raises(NotImplementedError):
        assert reversed(intervals)

    assert len(intervals) == 3


def test_collection_sorts_and_removes_duplicates() -> None:
    a = we.Interval(we.Moment(2020, 1, 1, 0, 0, 0), we.Moment(2020, 1, 2, 0, 0, 0))
    b = we.Interval(we.Moment(2020, 1, 2, 0, 0, 0), we.Moment(2020, 1, 3, 0, 0, 0))
    c = we.Interval(we.Moment(2020, 1, 3, 0, 0, 0), we.Moment(2020, 1, 4, 0, 0, 0))

    values = [a, b, c, a, b, c]
    intervals = we.Collection(values)
    assert list(intervals) == [a, b, c]
