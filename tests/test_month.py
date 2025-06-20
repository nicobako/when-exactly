import when_exactly as we
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_month_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=we.Month(2020, 1),
            custom_interval_type=we.Month,
            expected_next=we.Month(2020, 2),
            expected_start=we.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=we.Moment(2020, 2, 1, 0, 0, 0),
            expected_repr="Month(2020, 1)",
            expected_str="2020-01",
        )
    )


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
