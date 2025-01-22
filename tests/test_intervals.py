from assert_frozen import assert_frozen

import when_exactly as we


def test_intervals() -> None:
    values = [
        we.Interval(we.Moment(2020, 1, 1, 0, 0, 0), we.Moment(2020, 1, 2, 0, 0, 0)),
        we.Interval(we.Moment(2020, 1, 2, 0, 0, 0), we.Moment(2020, 1, 3, 0, 0, 0)),
        we.Interval(we.Moment(2020, 1, 3, 0, 0, 0), we.Moment(2020, 1, 4, 0, 0, 0)),
    ]
    intervals = we.Intervals(values)
    assert_frozen(intervals)
    assert list(intervals) == values
