import when_exactly as wnx
from tests.asserts import (
    CustomIntervalParams,
    assert_custom_interval_implemented_correctly,
)


def test_minute_implemented_correctly() -> None:
    assert_custom_interval_implemented_correctly(
        params=CustomIntervalParams(
            custom_interval=wnx.Minute(2020, 1, 1, 0, 0),
            custom_interval_type=wnx.Minute,
            expected_next=wnx.Minute(2020, 1, 1, 0, 1),
            expected_prev=wnx.Minute(2019, 12, 31, 23, 59),
            expected_start=wnx.Moment(2020, 1, 1, 0, 0, 0),
            expected_stop=wnx.Moment(2020, 1, 1, 0, 1, 0),
            expected_repr="Minute(2020, 1, 1, 0, 0)",
            expected_str="2020-01-01T00:00",
        )
    )


def test_minute_seconds() -> None:
    minute = wnx.Minute(2020, 1, 1, 0, 0)
    seconds = list(minute.seconds())
    assert len(seconds) == 60
    for i, second in enumerate(seconds):
        assert second == wnx.Second(2020, 1, 1, 0, 0, i)
    assert seconds[-1].start == wnx.Moment(2020, 1, 1, 0, 0, 59)
    assert seconds[-1].stop == wnx.Moment(2020, 1, 1, 0, 1, 0)


def test_minute_second() -> None:
    minute = wnx.Minute(2020, 1, 1, 0, 0)
    second = minute.second(0)
    assert second == wnx.Second(2020, 1, 1, 0, 0, 0)
    assert second.start == wnx.Moment(2020, 1, 1, 0, 0, 0)
    assert second.stop == wnx.Moment(2020, 1, 1, 0, 0, 1)
    assert second.minute() == minute
