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


def test_interval_months() -> None:
    start = we.Moment(2020, 1, 1, 0, 0, 0)
    stop = we.Moment(2020, 3, 1, 0, 0, 0)
    interval = we.Interval(start, stop)
    months = list(interval.months())
    assert len(months) == 2
    assert months[0] == we.Interval(
        we.Moment(2020, 1, 1, 0, 0, 0),
        we.Moment(2020, 2, 1, 0, 0, 0),
    )
    assert months[1] == we.Interval(
        we.Moment(2020, 2, 1, 0, 0, 0),
        we.Moment(2020, 3, 1, 0, 0, 0),
    )


def test_interval_months_empty() -> None:
    start = we.Moment(2020, 1, 1, 0, 0, 0)
    stop = we.Moment(2020, 1, 2, 0, 0, 0)
    interval = we.Interval(start, stop)
    months = list(interval.months())
    assert len(months) == 0
