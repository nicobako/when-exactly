import when_exactly as we


def test_year() -> None:
    year = we.year(2020)
    assert year.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert year.stop == we.Moment(2021, 1, 1, 0, 0, 0)
