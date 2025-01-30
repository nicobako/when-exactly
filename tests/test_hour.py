import when_exactly as we


def test_hour_minutes() -> None:
    hour = we.Hour(2020, 1, 1, 0)
    minutes = list(hour.minutes())
    assert len(minutes) == 60
    for i, minute in enumerate(minutes):
        assert minute == we.Minute(2020, 1, 1, 0, i)
    assert minutes[-1].start == we.Moment(2020, 1, 1, 0, 59, 0)
    assert minutes[-1].stop == we.Moment(2020, 1, 1, 1, 0, 0)


def test_next_hour() -> None:
    hour = we.Hour(2020, 1, 1, 0)
    assert next(hour) == we.Hour(2020, 1, 1, 1)
    assert next(next(hour)) == we.Hour(2020, 1, 1, 2)


def test_hour_day() -> None:
    hour = we.Hour(2020, 1, 1, 0)
    day = hour.day()
    assert day == we.Day(2020, 1, 1)
