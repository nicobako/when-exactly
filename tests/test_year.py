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
    assert len(weeks) == 53
    for i, week in enumerate(weeks):
        assert week == we.Week(2020, i + 1)
    assert weeks[-1].start == we.Moment(2020, 12, 28, 0, 0, 0)
    assert weeks[-1].stop == we.Moment(2021, 1, 4, 0, 0, 0)


def test_year_next() -> None:
    year = we.Year(2020)
    assert next(year) == we.Year(2021)
    assert next(next(year)) == we.Year(2022)
