import when_exactly as wnx
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_weeks_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=wnx.Weeks,
            interval_values=[
                wnx.Week(2020, 1),
                wnx.Week(2020, 2),
                wnx.Week(2020, 3),
            ],
            type_name="Weeks",
        )
    )


def test_weeks() -> None:
    weeks = wnx.Weeks(
        [
            wnx.Week(2020, 1),
            wnx.Week(2020, 2),
            wnx.Week(2020, 3),
        ]
    )
    assert isinstance(weeks, wnx.Weeks)
    assert isinstance(weeks, wnx.Collection)
