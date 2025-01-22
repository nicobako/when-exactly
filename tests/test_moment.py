import when_exactly as we
import datetime

def test_moment():
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    assert str(moment) == "2020-1-1 0:0:0"
    assert moment.year == 2020
    assert moment.month == 1
    assert moment.day == 1
    assert moment.hour == 0
    assert moment.minute == 0
    assert moment.second == 0
    assert moment == we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment != we.Moment(2020, 1, 1, 0, 0, 1)

def test_moment_to_datetime():
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment.to_datetime() == datetime.datetime(2020, 1, 1, 0, 0, 0)

def test_moment_from_datetime():
    dt = datetime.datetime(2020, 1, 1, 0, 0, 0)
    moment = we.Moment.from_datetime(dt)
    assert moment == we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment.to_datetime() == dt