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
def intervals(values: list[we.Interval]) -> we.Intervals[we.Interval]:
    return we.Intervals(values)


def test_intervals_collection_api(
    values: list[we.Interval], intervals: we.Intervals[we.Interval]
) -> None:
    assert list(intervals) == values
    assert list(intervals) == values

    assert values[0] in intervals
    assert intervals[0] == values[0]

    assert intervals[0:2] == we.Intervals(values[0:2])
    assert intervals == intervals

    with pytest.raises(NotImplementedError):
        assert reversed(intervals)
