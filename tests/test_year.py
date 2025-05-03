import pytest

import when_exactly as we


def test_year_months() -> None:
    year = we.Year(2020)
    months = year.months
    assert months == we.Months([we.Month(2020, i + 1) for i in range(12)])


@pytest.mark.parametrize(  # type: ignore
    "month_number",
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
)
def test_year_month(month_number: int) -> None:
    year = we.Year(2020)
    month = year.month(month_number)
    assert month == we.Month(2020, month_number)


def test_year_weeks() -> None:
    year = we.Year(2020)
    weeks = year.weeks
    assert weeks == we.Weeks([we.Week(2020, i + 1) for i in range(53)])


def test_year_days() -> None:
    year = we.Year(2020)
    days = year.days
    assert len(days) == 366
    assert days[0] == we.Day(2020, 1, 1)
    assert days[-1] == we.Day(2020, 12, 31)
