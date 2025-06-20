import when_exactly as we
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_days_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=we.Days,
            interval_values=[
                we.Day(2020, 1, 1),
                we.Day(2020, 1, 2),
                we.Day(2020, 1, 3),
            ],
            type_name="Days",
        )
    )


def test_initialization() -> None:
    days = we.Days(
        [
            we.Day(2020, 1, 1),
            we.Day(2020, 1, 2),
            we.Day(2020, 1, 3),
        ]
    )
    assert isinstance(days, we.Days)
    assert isinstance(days, we.Collection)


def test_months() -> None:
    days = we.Days(
        [
            we.Day(2020, 1, 1),
            we.Day(2020, 1, 2),
            we.Day(2020, 1, 3),
            we.Day(2020, 2, 1),
            we.Day(2020, 2, 2),
            we.Day(2020, 2, 3),
        ]
    )
    assert days.months == we.Months([we.Month(2020, 1), we.Month(2020, 2)])
