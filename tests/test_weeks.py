import when_exactly as we
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_weeks_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=we.Weeks,
            interval_values=[
                we.Week(2020, 1),
                we.Week(2020, 2),
                we.Week(2020, 3),
            ],
            type_name="Weeks",
        )
    )


def test_weeks() -> None:
    weeks = we.Weeks(
        [
            we.Week(2020, 1),
            we.Week(2020, 2),
            we.Week(2020, 3),
        ]
    )
    assert isinstance(weeks, we.Weeks)
    assert isinstance(weeks, we.Collection)
