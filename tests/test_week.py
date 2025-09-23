import when_exactly as wnx
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_week_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=wnx.Week(2020, 1),
            custom_interval_type=wnx.Week,
            expected_next=wnx.Week(2020, 2),
            expected_prev=wnx.Week(2019, 52),
            expected_start=wnx.Moment(2019, 12, 30, 0, 0, 0),
            expected_stop=wnx.Moment(2020, 1, 6, 0, 0, 0),
            expected_repr="Week(2020, 1)",
            expected_str="2020-W01",
        )
    )


def test_week_week_day() -> None:
    week = wnx.Week(2020, 1)
    assert week.week_day(1) == wnx.Weekday(2020, 1, 1)
    assert week.week_day(2) == wnx.Weekday(2020, 1, 2)
    assert week.week_day(7) == wnx.Weekday(2020, 1, 7)


def test_week_week_days() -> None:
    week = wnx.Week(2020, 1)
    week_days = week.week_days
    expected = wnx.Weekdays([wnx.Weekday(2020, 1, i) for i in range(1, 8)])
    assert week_days == expected


def test_week_days() -> None:
    week = wnx.Week(2020, 2)
    days = week.days
    expected = wnx.Days([wnx.Day(2020, 1, 5 + i) for i in range(1, 8)])
    assert days == expected
