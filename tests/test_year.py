from assert_frozen import assert_frozen

import when_exactly as we


def test_year() -> None:
    year = we.year(2020)
    assert_frozen(year)
    assert year.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert year.stop == we.Moment(2021, 1, 1, 0, 0, 0)
    assert str(year) == "2020"


def test_year_months() -> None:
    year = we.year(2020)
    months = list(year.months())
    assert len(months) == 12
    for i, month in enumerate(months):
        assert month == we.month(2020, i + 1)
    assert months[-1].start == we.Moment(2020, 12, 1, 0, 0, 0)
    assert months[-1].stop == we.Moment(2021, 1, 1, 0, 0, 0)


def test_year_month() -> None:
    year = we.year(2020)
    month = year.month(1)
    assert month == we.month(2020, 1)


def test_year_next() -> None:
    year = we.year(2020)
    assert next(year) == we.year(2021)
    assert next(next(year)) == we.year(2022)


def test_year_iso() -> None:
    year = we.year(2025)
    assert year.iso() == "2025"
