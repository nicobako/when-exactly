import when_exactly as we


def test_year_months() -> None:
    year = we.Year(2020)
    months = year.months()
    assert len(months) == 12
    for i, month in enumerate(months):
        assert month == we.Month(2020, i + 1)
    assert months[-1].start == we.Moment(2020, 12, 1, 0, 0, 0)
    assert months[-1].stop == we.Moment(2021, 1, 1, 0, 0, 0)


def test_year_month() -> None:
    year = we.Year(2020)
    month = year.month(1)
    assert month == we.Month(2020, 1)


def test_year_weeks() -> None:
    year = we.Year(2020)
    weeks = year.weeks()
    assert len(weeks) == 53
    for i, week in enumerate(weeks):
        assert week == we.Week(2020, i + 1)
    assert weeks[-1].start == we.Moment(2020, 12, 28, 0, 0, 0)
    assert weeks[-1].stop == we.Moment(2021, 1, 4, 0, 0, 0)


def test_year_next() -> None:
    year = we.Year(2020)
    assert next(year) == we.Year(2021)
    assert next(next(year)) == we.Year(2022)
