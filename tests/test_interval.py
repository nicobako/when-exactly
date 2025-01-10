from assert_frozen import assert_frozen
import when_exactly as we


def test_interval() -> None:
    start = we.Moment(2020, 1, 1, 0, 0, 0)
    stop = we.Moment(2021, 1, 1, 0, 0, 0)
    interval = we.Interval(start, stop)
    assert interval.start == start
    assert interval.stop == stop
    assert_frozen(interval)
