import when_exactly as wnx
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_hours_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=wnx.Hours,
            interval_values=[
                wnx.Hour(2020, 1, 1, 0),
                wnx.Hour(2020, 1, 1, 1),
                wnx.Hour(2020, 1, 1, 2),
            ],
            type_name="Hours",
        )
    )
