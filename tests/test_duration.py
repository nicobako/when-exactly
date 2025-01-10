import when_exactly as we
import dataclasses

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

def test_duration_frozen():
    duration = we.Duration()
    try:
        duration.years = 1 # type: ignore
    except dataclasses.FrozenInstanceError:
        pass
    else:
        assert False, "Expected a FrozenInstanceError"
