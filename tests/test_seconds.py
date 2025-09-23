import when_exactly as wnx
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_seconds_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=wnx.Seconds,
            interval_values=[
                wnx.Second(2020, 1, 1, 0, 0, 0),
                wnx.Second(2020, 1, 1, 0, 0, 1),
                wnx.Second(2020, 1, 1, 0, 0, 2),
            ],
            type_name="Seconds",
        )
    )
