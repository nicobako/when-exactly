from assert_frozen import assert_frozen

import when_exactly as we


def test_hour() -> None:
    hour = we.hour(2020, 1, 1, 0)
    assert_frozen(hour)
    assert hour.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert hour.stop == we.Moment(2020, 1, 1, 1, 0, 0)


def test_hour_minutes() -> None:
    hour = we.hour(2020, 1, 1, 0)
    minutes = list(hour.minutes())
    assert len(minutes) == 60
    for i, minute in enumerate(minutes):
        assert minute == we.minute(2020, 1, 1, 0, i)
    assert minutes[-1].start == we.Moment(2020, 1, 1, 0, 59, 0)
    assert minutes[-1].stop == we.Moment(2020, 1, 1, 1, 0, 0)
