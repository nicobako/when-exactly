import pytest

import when_exactly as wnx
from tests.asserts import assert_frozen


def test_interval() -> None:
    start = wnx.Moment(2020, 1, 1, 0, 0, 0)
    stop = wnx.Moment(2021, 1, 1, 0, 0, 0)
    interval = wnx.Interval(start, stop)
    assert interval.start == start
    assert interval.stop == stop
    assert_frozen(interval)


def test_interval_start_and_stop_cannot_ge() -> None:
    start = wnx.Moment(2020, 1, 1, 0, 0, 0)
    with pytest.raises(ValueError):
        wnx.Interval(start, start)
    with pytest.raises(ValueError):
        wnx.Interval(start, wnx.Moment(2019, 1, 1, 0, 0, 0))


def test_comparators() -> None:
    start = wnx.Moment(2020, 1, 1, 0, 0, 0)
    stop = wnx.Moment(2021, 1, 1, 0, 0, 0)
    interval = wnx.Interval(start, stop)
    eq_interval = wnx.Interval(start, stop)
    assert interval == eq_interval
    lt_intervals = [
        wnx.Interval(start, stop + wnx.Delta(seconds=-1)),
        wnx.Interval(start + wnx.Delta(seconds=-1), stop),
    ]
    for lt_interval in lt_intervals:
        assert lt_interval < interval
        assert lt_interval <= interval

    gt_intervals = [
        wnx.Interval(start, stop + wnx.Delta(seconds=1)),
        wnx.Interval(start + wnx.Delta(seconds=1), stop),
    ]
    for gt_interval in gt_intervals:
        assert gt_interval > interval
        assert gt_interval >= interval


def test_str() -> None:
    interval = wnx.Interval(
        wnx.Moment(2020, 1, 1, 0, 0, 0), wnx.Moment(2021, 1, 1, 0, 0, 0)
    )
    assert str(interval) == "2020-01-01T00:00:00/2021-01-01T00:00:00"
