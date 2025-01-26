from custom_interval import assert_custom_interval

import when_exactly as we


def test_day() -> None:
    assert_custom_interval(
        we.Day,
        we.Day(2020, 1, 1),
        we.Moment(2020, 1, 1, 0, 0, 0),
        we.Moment(2020, 1, 2, 0, 0, 0),
        "Day(2020, 1, 1)",
        "2020-01-01",
    )


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
