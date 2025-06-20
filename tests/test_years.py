import when_exactly as we
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_years_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=we.Years,
            interval_values=[
                we.Year(2020),
                we.Year(2021),
                we.Year(2023),
            ],
            type_name="Years",
        )
    )
