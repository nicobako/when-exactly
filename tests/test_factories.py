import when_exactly as we
import datetime

def test_now():
    now = we.now()
    assert isinstance(now, we.Moment)
    assert now.to_datetime() <= datetime.datetime.now()