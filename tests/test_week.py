import when_exactly as we


def test_week_week_day() -> None:
    week = we.Week(2020, 1)
    assert week.week_day(1) == we.WeekDay(2020, 1, 1)
    assert week.week_day(2) == we.WeekDay(2020, 1, 2)
    assert week.week_day(7) == we.WeekDay(2020, 1, 7)


def test_week_week_days() -> None:
    week = we.Week(2020, 1)
    week_days = week.week_days
    expected = we.WeekDays([we.WeekDay(2020, 1, i) for i in range(1, 8)])
    assert week_days == expected
