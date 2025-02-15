"""Test that custom intervals properly override base-class methods."""

from typing import Type

import pytest

import when_exactly as we
from tests.core.assert_frozen import assert_frozen


@pytest.mark.parametrize(
    [
        "custom_interval_type",
        "custom_interval",
        "expected_start",
        "expected_stop",
        "expected_repr",
        "expected_str",
    ],
    [
        (
            we.Year,
            we.Year(2020),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2021, 1, 1, 0, 0, 0),
            "Year(2020)",
            "2020",
        ),
        (
            we.Month,
            we.Month(2020, 1),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 2, 1, 0, 0, 0),
            "Month(2020, 1)",
            "2020-01",
        ),
        (
            we.Week,
            we.Week(2020, 1),
            we.Moment(2019, 12, 30, 0, 0, 0),
            we.Moment(2020, 1, 6, 0, 0, 0),
            "Week(2020, 1)",
            "2020-W01",
        ),
        (
            we.Day,
            we.Day(2020, 1, 1),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 2, 0, 0, 0),
            "Day(2020, 1, 1)",
            "2020-01-01",
        ),
        (
            we.Hour,
            we.Hour(2020, 1, 1, 0),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 1, 1, 0, 0),
            "Hour(2020, 1, 1, 0)",
            "2020-01-01T00",
        ),
        (
            we.Minute,
            we.Minute(2020, 1, 1, 0, 0),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 1, 0, 1, 0),
            "Minute(2020, 1, 1, 0, 0)",
            "2020-01-01T00:00",
        ),
        (
            we.Second,
            we.Second(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 1, 0, 0, 1),
            "Second(2020, 1, 1, 0, 0, 0)",
            "2020-01-01T00:00:00",
        ),
    ],
)  # type: ignore
def test_custom_interval(
    custom_interval_type: Type[we.CustomInterval],
    custom_interval: we.CustomInterval,
    expected_start: we.Moment,
    expected_stop: we.Moment,
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
