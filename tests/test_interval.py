import pytest
from assert_frozen import assert_frozen

import when_exactly as we


def test_interval() -> None:
    start = we.Moment(2020, 1, 1, 0, 0, 0)
    stop = we.Moment(2021, 1, 1, 0, 0, 0)
    interval = we.Interval(start, stop)
    assert interval.start == start
    assert interval.stop == stop
    assert_frozen(interval)


def test_interval_start_and_stop_cannot_ge() -> None:
    start = we.Moment(2020, 1, 1, 0, 0, 0)
    with pytest.raises(ValueError):
        we.Interval(start, start)
    with pytest.raises(ValueError):
        we.Interval(start, we.Moment(2019, 1, 1, 0, 0, 0))


def test_comparators() -> None:
    start = we.Moment(2020, 1, 1, 0, 0, 0)
    stop = we.Moment(2021, 1, 1, 0, 0, 0)
    interval = we.Interval(start, stop)
    eq_interval = we.Interval(start, stop)
    assert interval == eq_interval
    lt_intervals = [
        we.Interval(start, stop + we.Delta(seconds=-1)),
        we.Interval(start + we.Delta(seconds=-1), stop),
    ]
    for lt_interval in lt_intervals:
        assert lt_interval < interval
        assert lt_interval <= interval

    gt_intervals = [
        we.Interval(start, stop + we.Delta(seconds=1)),
        we.Interval(start + we.Delta(seconds=1), stop),
    ]
    for gt_interval in gt_intervals:
        assert gt_interval > interval
        assert gt_interval >= interval
