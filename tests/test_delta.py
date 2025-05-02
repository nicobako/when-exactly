import when_exactly as we
from tests.core.assert_frozen import assert_frozen


def test_delta() -> None:
    duration = we.Delta(
        years=1,
        months=2,
        weeks=3,
        days=2,
        hours=3,
        minutes=4,
        seconds=30,
    )
    assert_frozen(duration)
    assert duration.years == 1
    assert duration.months == 2
    assert duration.weeks == 3
    assert duration.days == 2
    assert duration.hours == 3
    assert duration.minutes == 4
    assert duration.seconds == 30
