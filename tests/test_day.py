import when_exactly as we
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_day_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=we.Day(2020, 1, 1),
            custom_interval_type=we.Day,
            expected_next=we.Day(2020, 1, 2),
            expected_start=we.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=we.Moment(2020, 1, 2, 0, 0, 0),
            expected_repr="Day(2020, 1, 1)",
            expected_str="2020-01-01",
            expected_prev=we.Day(2019, 12, 31),
        )
    )

    d = we.Day(2020, 1, 1)
    d.next


def test_day_hour() -> None:
    day = we.Day(2020, 1, 1)
    for i in range(24):
        hour = day.hour(i)
        assert hour == we.Hour(2020, 1, 1, i)
        assert hour.start == we.Moment(2020, 1, 1, i, 0, 0)
        assert hour.day() == day


def test_day_month() -> None:
    day = we.Day(2020, 1, 1)
    month = day.month
    assert month == we.Month(2020, 1)


def test_day_week() -> None:
    day = we.Day(2020, 1, 1)
    week = day.week
    assert week == we.Week(2020, 1)


def test_day_ordinal_day() -> None:
    day = we.Day(2020, 1, 1)
    ordinal_day = we.OrdinalDay(2020, 1)
    assert day.ordinal_day == ordinal_day


def test_day_week_day() -> None:
    day = we.Day(2025, 9, 5)  # This is a Wednesday
    weekday = day.weekday
    assert weekday == we.WeekDay(2025, 36, 5)
