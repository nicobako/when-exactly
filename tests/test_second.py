import when_exactly as wnx
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_second_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=wnx.Second(2020, 1, 1, 0, 0, 0),
            custom_interval_type=wnx.Second,
            expected_prev=wnx.Second(2019, 12, 31, 23, 59, 59),
            expected_next=wnx.Second(2020, 1, 1, 0, 0, 1),
            expected_start=wnx.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=wnx.Moment(2020, 1, 1, 0, 0, 1),
            expected_repr="Second(2020, 1, 1, 0, 0, 0)",
            expected_str="2020-01-01T00:00:00",
        )
    )


def test_assert_second_minute() -> None:
    second = wnx.Second(2020, 1, 1, 0, 0, 0)
    minute = second.minute()
    assert isinstance(minute, wnx.Minute)
    assert minute.start == wnx.Moment(2020, 1, 1, 0, 0, 0)
    assert minute.stop == wnx.Moment(2020, 1, 1, 0, 1, 0)


def test_second_end_of_minute() -> None:
    second = wnx.Second(2020, 1, 1, 0, 0, 59)
    assert second.stop == wnx.Moment(2020, 1, 1, 0, 1, 0)


def test_from_moment() -> None:
    moment = wnx.Moment(2020, 1, 1, 0, 0, 0)
    second = wnx.Second.from_moment(moment)
    assert second == wnx.Second(2020, 1, 1, 0, 0, 0)
