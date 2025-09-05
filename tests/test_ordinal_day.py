import when_exactly as we
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_ordinal_day_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=we.OrdinalDay(
                2020,
                1,
            ),
            custom_interval_type=we.OrdinalDay,
            expected_next=we.OrdinalDay(2020, 2),
            expected_prev=we.OrdinalDay(2019, 365),
            expected_start=we.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=we.Moment(2020, 1, 2, 0, 0, 0),
            expected_repr="OrdinalDay(2020, 1)",
            expected_str="2020-001",
        )
    )
