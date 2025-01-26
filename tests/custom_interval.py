from typing import Type

from assert_frozen import assert_frozen

from when_exactly.custom_interval import CustomInterval
from when_exactly.moment import Moment


def assert_custom_interval(
    custom_interval_type: Type[CustomInterval],
    custom_interval: CustomInterval,
    expected_start: Moment,
    expected_stop: Moment,
    expected_repr: str,
    expected_str: str,
) -> None:
    assert_frozen(custom_interval)
    assert custom_interval.start == expected_start
    assert custom_interval.stop == expected_stop
    assert repr(custom_interval) == expected_repr
    assert str(custom_interval) == expected_str
    assert custom_interval_type.from_moment(expected_start) == custom_interval
    assert custom_interval_type.from_moment(expected_stop) == next(custom_interval)
