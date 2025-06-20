import when_exactly as we
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_seconds_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=we.Seconds,
            interval_values=[
                we.Second(2020, 1, 1, 0, 0, 0),
                we.Second(2020, 1, 1, 0, 0, 1),
                we.Second(2020, 1, 1, 0, 0, 2),
            ],
            type_name="Seconds",
        )
    )
