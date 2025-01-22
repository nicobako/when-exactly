import when_exactly as we
import dataclasses
from assert_frozen import assert_frozen
import datetime

def test_duration():
    duration = we.Duration(
        years=1, 
        months=2,
        weeks=3,
        days=2,
        hours=3,
        minutes=4,
        seconds=30,
    )
    assert duration.years == 1
    assert duration.months == 2
    assert duration.weeks == 3
    assert duration.days == 2
    assert duration.hours == 3
    assert duration.minutes == 4
    assert duration.seconds == 30
    assert_frozen(duration)

def test_add_durations():
    duration1 = we.Duration(
        years=1, 
        months=2,
        weeks=3,
        days=2,
        hours=3,
        minutes=4,
        seconds=30,
    )
    duration2 = we.Duration(
        years=2, 
        months=3,
        weeks=5,
        days=7,
        hours=25,
        minutes=7,
        seconds=55,
    )
    assert duration1 + duration2 == we.Duration(
        years=duration1.years + duration2.years, 
        months=duration1.months + duration2.months,
        weeks=duration1.weeks + duration2.weeks,
        days=duration1.days + duration2.days,
        hours=duration1.hours + duration2.hours,
        minutes= duration1.minutes + duration2.minutes,
        seconds=duration1.seconds + duration2.seconds,
    )