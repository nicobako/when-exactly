import when_exactly as wnx
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_days_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=wnx.Days,
            interval_values=[
                wnx.Day(2020, 1, 1),
                wnx.Day(2020, 1, 2),
                wnx.Day(2020, 1, 3),
            ],
            type_name="Days",
        )
    )


def test_initialization() -> None:
    days = wnx.Days(
        [
            wnx.Day(2020, 1, 1),
            wnx.Day(2020, 1, 2),
            wnx.Day(2020, 1, 3),
        ]
    )
    assert isinstance(days, wnx.Days)
    assert isinstance(days, wnx.Collection)


def test_months() -> None:
    days = wnx.Days(
        [
            wnx.Day(2020, 1, 1),
            wnx.Day(2020, 1, 2),
            wnx.Day(2020, 1, 3),
            wnx.Day(2020, 2, 1),
            wnx.Day(2020, 2, 2),
            wnx.Day(2020, 2, 3),
        ]
    )
    assert days.months == wnx.Months([wnx.Month(2020, 1), wnx.Month(2020, 2)])
