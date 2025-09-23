import when_exactly as wnx
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_month_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=wnx.Month(2020, 1),
            custom_interval_type=wnx.Month,
            expected_next=wnx.Month(2020, 2),
            expected_prev=wnx.Month(2019, 12),
            expected_start=wnx.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=wnx.Moment(2020, 2, 1, 0, 0, 0),
            expected_repr="Month(2020, 1)",
            expected_str="2020-01",
        )
    )


def test_month_days() -> None:
    month = wnx.Month(2020, 1)
    days = list(month.days())
    assert len(days) == 31
    for i, day in enumerate(days):
        assert day == wnx.Day(2020, 1, i + 1)
    assert days[-1].start == wnx.Moment(2020, 1, 31, 0, 0, 0)
    assert days[-1].stop == wnx.Moment(2020, 2, 1, 0, 0, 0)


def test_month_day() -> None:
    month = wnx.Month(2020, 1)
    day = month.day(1)
    assert day == wnx.Day(2020, 1, 1)
