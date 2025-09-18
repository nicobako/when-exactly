import when_exactly as we
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_week_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=we.Week(2020, 1),
            custom_interval_type=we.Week,
            expected_next=we.Week(2020, 2),
            expected_prev=we.Week(2019, 52),
            expected_start=we.Moment(2019, 12, 30, 0, 0, 0),
            expected_stop=we.Moment(2020, 1, 6, 0, 0, 0),
            expected_repr="Week(2020, 1)",
            expected_str="2020-W01",
        )
    )


def test_week_week_day() -> None:
    week = we.Week(2020, 1)
    assert week.week_day(1) == we.Weekday(2020, 1, 1)
    assert week.week_day(2) == we.Weekday(2020, 1, 2)
    assert week.week_day(7) == we.Weekday(2020, 1, 7)


def test_week_week_days() -> None:
    week = we.Week(2020, 1)
    week_days = week.week_days
    expected = we.Weekdays([we.Weekday(2020, 1, i) for i in range(1, 8)])
    assert week_days == expected


def test_week_days() -> None:
    week = we.Week(2020, 2)
    days = week.days
    expected = we.Days([we.Day(2020, 1, 5 + i) for i in range(1, 8)])
    assert days == expected
