from assert_frozen import assert_frozen

import when_exactly as we


def test_day() -> None:
    day = we.Day(2020, 1, 1)
    assert_frozen(day)
    assert day.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert day.stop == we.Moment(2020, 1, 2, 0, 0, 0)
    assert repr(day) == "Day(2020, 1, 1)"


def test_day_hours() -> None:
    day = we.Day(2020, 1, 1)
    hours = list(day.hours())
    assert len(hours) == 24
    for i, hour in enumerate(hours):
        assert hour == we.Hour(2020, 1, 1, i)
    assert hours[-1].start == we.Moment(2020, 1, 1, 23, 0, 0)
    assert hours[-1].stop == we.Moment(2020, 1, 2, 0, 0, 0)


def test_day_hour() -> None:
    day = we.Day(2020, 1, 1)
    for i in range(24):
        hour = day.hour(i)
        assert hour == we.Hour(2020, 1, 1, i)
        assert hour.start == we.Moment(2020, 1, 1, i, 0, 0)
        assert hour.day() == day


def test_day_months() -> None:
    day = we.Day(2020, 1, 1)
    month = day.month()
    assert month == we.Month(2020, 1)


def test_day_iso() -> None:
    day = we.Day(2020, 1, 1)
    assert day.iso() == "2020-01-01"
