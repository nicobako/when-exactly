"""Test that custom intervals properly override base-class methods."""

from dataclasses import dataclass
from typing import Type

import pytest

import when_exactly as we
from tests.core.assert_frozen import assert_frozen


@dataclass
class Params:
    custom_interval_type: Type[we.CustomInterval]
    custom_interval: we.CustomInterval
    expected_start: we.Moment
    expected_stop: we.Moment
    expected_repr: str
    expected_str: str
    expected_next: we.CustomInterval


@pytest.mark.parametrize(
    "params",
    [
        Params(
            we.Year,
            we.Year(2020),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2021, 1, 1, 0, 0, 0),
            "Year(2020)",
            "2020",
            we.Year(2021),
        ),
        Params(
            we.Month,
            we.Month(2020, 1),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 2, 1, 0, 0, 0),
            "Month(2020, 1)",
            "2020-01",
            we.Month(2020, 2),
        ),
        Params(
            we.Week,
            we.Week(2020, 1),
            we.Moment(2019, 12, 30, 0, 0, 0),
            we.Moment(2020, 1, 6, 0, 0, 0),
            "Week(2020, 1)",
            "2020-W01",
            we.Week(2020, 2),
        ),
        Params(
            we.Day,
            we.Day(2020, 1, 1),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 2, 0, 0, 0),
            "Day(2020, 1, 1)",
            "2020-01-01",
            we.Day(2020, 1, 2),
        ),
        Params(
            we.WeekDay,
            we.WeekDay(2025, 20, 5),
            we.Moment(2025, 5, 16, 0, 0, 0),
            we.Moment(2025, 5, 17, 0, 0, 0),
            "WeekDay(2025, 20, 5)",
            "2025-W20-5",
            we.WeekDay(2025, 20, 6),
        ),
        Params(
            we.OrdinalDay,
            we.OrdinalDay(2020, 1),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 2, 0, 0, 0),
            "OrdinalDay(2020, 1)",
            "2020-001",
            we.OrdinalDay(2020, 2),
        ),
        Params(
            we.Hour,
            we.Hour(2020, 1, 1, 0),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 1, 1, 0, 0),
            "Hour(2020, 1, 1, 0)",
            "2020-01-01T00",
            we.Hour(2020, 1, 1, 1),
        ),
        Params(
            we.Minute,
            we.Minute(2020, 1, 1, 0, 0),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 1, 0, 1, 0),
            "Minute(2020, 1, 1, 0, 0)",
            "2020-01-01T00:00",
            we.Minute(2020, 1, 1, 0, 1),
        ),
        Params(
            we.Second,
            we.Second(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 1, 0, 0, 0),
            we.Moment(2020, 1, 1, 0, 0, 1),
            "Second(2020, 1, 1, 0, 0, 0)",
            "2020-01-01T00:00:00",
            we.Second(2020, 1, 1, 0, 0, 1),
        ),
    ],
)  # type: ignore
def test_custom_interval(
    params: Params,
) -> None:
    """Test that custom intervals properly override base-class methods."""
    assert_frozen(params.custom_interval)
    assert params.custom_interval.start == params.expected_start
    assert params.custom_interval.stop == params.expected_stop
    assert repr(params.custom_interval) == params.expected_repr
    assert str(params.custom_interval) == params.expected_str
    assert (
        params.custom_interval_type.from_moment(params.expected_start)
        == params.custom_interval
    )
    assert params.custom_interval_type.from_moment(params.expected_stop) == next(
        params.custom_interval
    )
    assert next(params.custom_interval) == params.expected_next
    assert params.custom_interval.next == params.expected_next
