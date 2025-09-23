import when_exactly as wnx
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_week_day_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=wnx.Weekday(2020, 1, 1),
            custom_interval_type=wnx.Weekday,
            expected_next=wnx.Weekday(2020, 1, 2),
            expected_prev=wnx.Weekday(2019, 52, 7),
            expected_start=wnx.Moment(2019, 12, 30, 0, 0, 0),
            expected_stop=wnx.Moment(2019, 12, 31, 0, 0, 0),
            expected_repr="Weekday(2020, 1, 1)",
            expected_str="2020-W01-1",
        )
    )


def test_week_day_next_edge_cases() -> None:
    sunday = wnx.Weekday(2025, 20, 7)
    assert sunday.next == wnx.Weekday(2025, 21, 1)

    last_week_day_of_year = wnx.Weekday(2024, 52, 7)
    assert last_week_day_of_year.next == wnx.Weekday(2025, 1, 1)


def test_week_day_week() -> None:
    week_day = wnx.Weekday(2025, 5, 3)
    assert week_day.week == wnx.Week(2025, 5)

    # wnx.Weekday(2025,1,1) is 2024-12-30
    assert wnx.Weekday(2025, 1, 1).week == wnx.Week(
        2025, 1
    )  # day with different month-day


def test_weed_day_to_day() -> None:
    week_day = wnx.Weekday(2025, 1, 1)
    assert week_day.to_day() == wnx.Day(2024, 12, 30)
