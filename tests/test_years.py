import when_exactly as wnx
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_years_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=wnx.Years,
            interval_values=[
                wnx.Year(2020),
                wnx.Year(2021),
                wnx.Year(2023),
            ],
            type_name="Years",
        )
    )
