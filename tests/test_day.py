import when_exactly as we


def test_day_hour() -> None:
    day = we.Day(2020, 1, 1)
    for i in range(24):
        hour = day.hour(i)
        assert hour == we.Hour(2020, 1, 1, i)
        assert hour.start == we.Moment(2020, 1, 1, i, 0, 0)
        assert hour.day() == day


def test_day_month() -> None:
    day = we.Day(2020, 1, 1)
    month = day.month()
    assert month == we.Month(2020, 1)


def test_day_week() -> None:
    day = we.Day(2020, 1, 1)
    week = day.week()
    assert week == we.Week(2020, 1)
