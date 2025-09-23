import when_exactly as wnx
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_minutes_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=wnx.Minutes,
            interval_values=[
                wnx.Minute(2020, 1, 1, 0, 0),
                wnx.Minute(2020, 1, 1, 0, 1),
                wnx.Minute(2020, 1, 1, 0, 2),
            ],
            type_name="Minutes",
        )
    )
