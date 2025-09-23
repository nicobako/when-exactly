import when_exactly as wnx
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_hour_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=wnx.Hour(2020, 1, 1, 0),
            custom_interval_type=wnx.Hour,
            expected_next=wnx.Hour(2020, 1, 1, 1),
            expected_prev=wnx.Hour(2019, 12, 31, 23),
            expected_start=wnx.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=wnx.Moment(2020, 1, 1, 1, 0, 0),
            expected_repr="Hour(2020, 1, 1, 0)",
            expected_str="2020-01-01T00",
        )
    )


def test_hour_minutes() -> None:
    hour = wnx.Hour(2020, 1, 1, 0)
    minutes = list(hour.minutes())
    assert len(minutes) == 60
    for i, minute in enumerate(minutes):
        assert minute == wnx.Minute(2020, 1, 1, 0, i)
    assert minutes[-1].start == wnx.Moment(2020, 1, 1, 0, 59, 0)
    assert minutes[-1].stop == wnx.Moment(2020, 1, 1, 1, 0, 0)


def test_hour_day() -> None:
    hour = wnx.Hour(2020, 1, 1, 0)
    day = hour.day()
    assert day == wnx.Day(2020, 1, 1)


def test_hour_minute() -> None:
    hour = wnx.Hour(2020, 1, 1, 0)
    assert hour.minute(0) == wnx.Minute(2020, 1, 1, 0, 0)
    assert hour.minute(59) == wnx.Minute(2020, 1, 1, 0, 59)
