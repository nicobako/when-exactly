import when_exactly as we
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_hour_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=we.Hour(2020, 1, 1, 0),
            custom_interval_type=we.Hour,
            expected_next=we.Hour(2020, 1, 1, 1),
            expected_prev=we.Hour(2019, 12, 31, 23),
            expected_start=we.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=we.Moment(2020, 1, 1, 1, 0, 0),
            expected_repr="Hour(2020, 1, 1, 0)",
            expected_str="2020-01-01T00",
        )
    )


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


def test_hour_minute() -> None:
    hour = we.Hour(2020, 1, 1, 0)
    assert hour.minute(0) == we.Minute(2020, 1, 1, 0, 0)
    assert hour.minute(59) == we.Minute(2020, 1, 1, 0, 59)
