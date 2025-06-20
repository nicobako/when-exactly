import when_exactly as we
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_minutes_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=we.Minutes,
            interval_values=[
                we.Minute(2020, 1, 1, 0, 0),
                we.Minute(2020, 1, 1, 0, 1),
                we.Minute(2020, 1, 1, 0, 2),
            ],
            type_name="Minutes",
        )
    )
