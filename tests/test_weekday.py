import when_exactly as we
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_week_day_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=we.WeekDay(2020, 1, 1),
            custom_interval_type=we.WeekDay,
            expected_next=we.WeekDay(2020, 1, 2),
            expected_prev=we.WeekDay(2019, 52, 7),
            expected_start=we.Moment(2019, 12, 30, 0, 0, 0),
            expected_stop=we.Moment(2019, 12, 31, 0, 0, 0),
            expected_repr="WeekDay(2020, 1, 1)",
            expected_str="2020-W01-1",
        )
    )


def test_week_day_next_edge_cases() -> None:
    sunday = we.WeekDay(2025, 20, 7)
    assert sunday.next == we.WeekDay(2025, 21, 1)

    last_week_day_of_year = we.WeekDay(2024, 52, 7)
    assert last_week_day_of_year.next == we.WeekDay(2025, 1, 1)


def test_week_day_week() -> None:
    week_day = we.WeekDay(2025, 5, 3)
    assert week_day.week == we.Week(2025, 5)

    # we.WeekDay(2025,1,1) is 2024-12-30
    assert we.WeekDay(2025, 1, 1).week == we.Week(
        2025, 1
    )  # day with different month-day


def test_weed_day_to_day() -> None:
    week_day = we.WeekDay(2025, 1, 1)
    assert week_day.to_day() == we.Day(2024, 12, 30)
