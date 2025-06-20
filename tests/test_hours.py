import when_exactly as we
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_hours_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=we.Hours,
            interval_values=[
                we.Hour(2020, 1, 1, 0),
                we.Hour(2020, 1, 1, 1),
                we.Hour(2020, 1, 1, 2),
            ],
            type_name="Hours",
        )
    )
