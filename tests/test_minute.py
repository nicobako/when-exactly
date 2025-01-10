from assert_frozen import assert_frozen

import when_exactly as we


def test_minute() -> None:
    minute = we.minute(2020, 1, 1, 0, 0)
    assert_frozen(minute)
    assert minute.start == we.Moment(2020, 1, 1, 0, 0, 0)
    assert minute.stop == we.Moment(2020, 1, 1, 0, 1, 0)


def test_minute_seconds() -> None:
    minute = we.minute(2020, 1, 1, 0, 0)
    seconds = list(minute.seconds())
    assert len(seconds) == 60
    for i, second in enumerate(seconds):
        assert second == we.second(2020, 1, 1, 0, 0, i)
    assert seconds[-1].start == we.Moment(2020, 1, 1, 0, 0, 59)
    assert seconds[-1].stop == we.Moment(2020, 1, 1, 0, 1, 0)