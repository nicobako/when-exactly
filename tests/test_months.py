import when_exactly as we
from tests.asserts import (
    CustomCollectionParams,
    assert_custom_collection_implemented_correctly,
)


def test_months_implemented_correctly() -> None:
    assert_custom_collection_implemented_correctly(
        params=CustomCollectionParams(
            collection_type=we.Months,
            interval_values=[
                we.Month(2020, 1),
                we.Month(2020, 2),
                we.Month(2020, 9),
                we.Month(2020, 11),
                we.Month(2020, 12),
            ],
            type_name="Months",
        )
    )
