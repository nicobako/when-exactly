import when_exactly as wnx
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_months_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=wnx.Months,
            interval_values=[
                wnx.Month(2020, 1),
                wnx.Month(2020, 2),
                wnx.Month(2020, 9),
                wnx.Month(2020, 11),
                wnx.Month(2020, 12),
            ],
            type_name="Months",
        )
    )
