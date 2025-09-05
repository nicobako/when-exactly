import when_exactly as we
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_minute_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=we.Minute(2020, 1, 1, 0, 0),
            custom_interval_type=we.Minute,
            expected_next=we.Minute(2020, 1, 1, 0, 1),
            expected_prev=we.Minute(2019, 12, 31, 23, 59),
            expected_start=we.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=we.Moment(2020, 1, 1, 0, 1, 0),
            expected_repr="Minute(2020, 1, 1, 0, 0)",
            expected_str="2020-01-01T00:00",
        )
    )


def test_minute_seconds() -> None:
    minute = we.Minute(2020, 1, 1, 0, 0)
    seconds = list(minute.seconds())
    assert len(seconds) == 60
    for i, second in enumerate(seconds):
        assert second == we.Second(2020, 1, 1, 0, 0, i)
    assert seconds[-1].start == we.Moment(2020, 1, 1, 0, 0, 59)
    assert seconds[-1].stop == we.Moment(2020, 1, 1, 0, 1, 0)


def test_minute_second() -> None:
    minute = we.Minute(2020, 1, 1, 0, 0)
    second = minute.second(0)
    assert second == we.Second(2020, 1, 1, 0, 0, 0)
    assert second.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert second.stop == we.Moment(2020, 1, 1, 0, 0, 1)
    assert second.minute() == minute


def test_minute_next() -> None:
    minute = we.Minute(2020, 1, 1, 0, 0)
    assert next(minute) == we.Minute(2020, 1, 1, 0, 1)
    assert next(next(minute)) == we.Minute(2020, 1, 1, 0, 2)
