import pytest

import when_exactly as wnx
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_year_implemented_correcly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=wnx.Year(2020),
            custom_interval_type=wnx.Year,
            expected_next=wnx.Year(2021),
            expected_prev=wnx.Year(2019),
            expected_start=wnx.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=wnx.Moment(2021, 1, 1, 0, 0, 0),
            expected_repr="Year(2020)",
            expected_str="2020",
        )
    )


def test_year_months() -> None:
    year = wnx.Year(2020)
    months = year.months
    assert months == wnx.Months([wnx.Month(2020, i + 1) for i in range(12)])


@pytest.mark.parametrize(  # type: ignore
    "month_number",
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
)
def test_year_month(month_number: int) -> None:
    year = wnx.Year(2020)
    month = year.month(month_number)
    assert month == wnx.Month(2020, month_number)


def test_year_weeks() -> None:
    year = wnx.Year(2020)
    weeks = year.weeks
    assert weeks == wnx.Weeks([wnx.Week(2020, i + 1) for i in range(53)])


def test_year_week() -> None:
    year = wnx.Year(2020)
    week = year.week(1)
    assert week == wnx.Week(2020, 1)

    # Test for a week that crosses into the next year
    week = year.week(53)
    assert week == wnx.Week(2020, 53)

    # wnx.Weekday(2025,1,1) is 2024-12-30
    edge_case_year = wnx.Year(2025)
    week = edge_case_year.week(1)
    assert week == wnx.Week(2025, 1)  # day with different month-day
    assert week.week_day(1).to_day() == wnx.Day(2024, 12, 30)


def test_year_ordinal_day() -> None:
    year = wnx.Year(2020)
    ordinal_day = year.ordinal_day(1)
    assert ordinal_day == wnx.OrdinalDay(2020, 1)

    # Test for the last day of the year
    ordinal_day = year.ordinal_day(366)
    assert ordinal_day == wnx.OrdinalDay(2020, 366)

    # Test for a non-leap year
    non_leap_year = wnx.Year(2021)
    ordinal_day = non_leap_year.ordinal_day(365)
    assert ordinal_day == wnx.OrdinalDay(2021, 365)  # Last day of a non-leap year
