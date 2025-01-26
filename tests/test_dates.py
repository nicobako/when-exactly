import when_exactly as we


def test_days() -> None:
    days = we.Days(
        [
            we.Day(2020, 1, 1),
            we.Day(2020, 1, 2),
            we.Day(2020, 1, 3),
        ]
    )
    assert isinstance(days, we.Days)
    assert isinstance(days, we.Intervals)


def test_days_months() -> None:
    days = we.Days(
        [
            we.Day(2020, 1, 1),
            we.Day(2020, 1, 2),
            we.Day(2020, 1, 3),
        ]
    )
    months = days.months()
    assert len(months) == 1
    assert months[0] == we.Month(2020, 1)
