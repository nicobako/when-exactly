from assert_frozen import assert_frozen

import when_exactly as we


def test_year() -> None:
    year = we.year(2020)
    assert year.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert year.stop == we.Moment(2021, 1, 1, 0, 0, 0)
    assert_frozen(year)

    months = list(year.months())
    assert len(months) == 12


def test_year_month() -> None:
    # year = we.year(2020)
    # month = year.month(1)
    pass
