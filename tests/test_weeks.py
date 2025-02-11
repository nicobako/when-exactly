import when_exactly as we


def test_weeks() -> None:
    weeks = we.Weeks(
        [
            we.Week(2020, 1),
            we.Week(2020, 2),
            we.Week(2020, 3),
        ]
    )
    assert isinstance(weeks, we.Weeks)
    assert isinstance(weeks, we.Intervals)
