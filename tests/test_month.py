from assert_frozen import assert_frozen

import when_exactly as we


def test_month() -> None:
    month = we.Month(2020, 1)
    assert_frozen(month)
    assert month.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert month.stop == we.Moment(2020, 2, 1, 0, 0, 0)


def test_month_days() -> None:
    month = we.Month(2020, 1)
    days = list(month.days())
    assert len(days) == 31
    for i, day in enumerate(days):
        assert day == we.Day(2020, 1, i + 1)
    assert days[-1].start == we.Moment(2020, 1, 31, 0, 0, 0)
    assert days[-1].stop == we.Moment(2020, 2, 1, 0, 0, 0)


def test_month_day() -> None:
    month = we.Month(2020, 1)
    day = month.day(1)
    assert day == we.Day(2020, 1, 1)


def test_month_next() -> None:
    month = we.Month(2020, 1)
    assert next(month) == we.Month(2020, 2)
    assert next(next(month)) == we.Month(2020, 3)


def test_month_iso() -> None:
    month = we.Month(2023, 5)
    expected_iso = "2023-05"
    assert month.iso() == expected_iso
