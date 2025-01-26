from assert_frozen import assert_frozen
from custom_interval import assert_custom_interval

import when_exactly as we


def test_minute() -> None:
    assert_custom_interval(
        we.Minute,
        we.Minute(2020, 1, 1, 0, 0),
        we.Moment(2020, 1, 1, 0, 0, 0),
        we.Moment(2020, 1, 1, 0, 1, 0),
        "Minute(2020, 1, 1, 0, 0)",
        "2020-01-01T00:00",
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
    assert_frozen(second)
    assert second.minute() == minute


def test_minute_next() -> None:
    minute = we.Minute(2020, 1, 1, 0, 0)
    assert next(minute) == we.Minute(2020, 1, 1, 0, 1)
    assert next(next(minute)) == we.Minute(2020, 1, 1, 0, 2)
