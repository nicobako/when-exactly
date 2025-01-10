import datetime

import when_exactly as we


def test_now() -> None:
    now = we.now()
    assert isinstance(now, we.Moment)
    assert now.to_datetime() <= datetime.datetime.now()
