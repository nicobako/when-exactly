import when_exactly as we
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_second_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=we.Second(2020, 1, 1, 0, 0, 0),
            custom_interval_type=we.Second,
            expected_next=we.Second(2020, 1, 1, 0, 0, 1),
            expected_start=we.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=we.Moment(2020, 1, 1, 0, 0, 1),
            expected_repr="Second(2020, 1, 1, 0, 0, 0)",
            expected_str="2020-01-01T00:00:00",
        )
    )


def test_assert_second_minute() -> None:
    second = we.Second(2020, 1, 1, 0, 0, 0)
    minute = second.minute()
    assert isinstance(minute, we.Minute)
    assert minute.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert minute.stop == we.Moment(2020, 1, 1, 0, 1, 0)


def test_second_end_of_minute() -> None:
    second = we.Second(2020, 1, 1, 0, 0, 59)
    assert second.stop == we.Moment(2020, 1, 1, 0, 1, 0)


def test_second_next() -> None:
    second = we.Second(2020, 1, 1, 0, 0, 0)
    assert next(second) == we.Second(2020, 1, 1, 0, 0, 1)


def test_from_moment() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    second = we.Second.from_moment(moment)
    assert second == we.Second(2020, 1, 1, 0, 0, 0)
