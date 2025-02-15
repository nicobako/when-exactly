from typing import Type

import pytest

import when_exactly as we


@pytest.mark.parametrize(
    [
        "intervals_type",
        "interval_values",
    ],
    [
        (
            we.Years,
            [we.Year(2020), we.Year(2023)],
        ),
        (
            we.Months,
            [we.Month(2020, 1), we.Month(2020, 3)],
        ),
        (
            we.Weeks,
            [we.Week(2020, 1), we.Week(2020, 3)],
        ),
        (
            we.Days,
            [we.Day(2020, 1, 1), we.Day(2020, 1, 3)],
        ),
        (
            we.Hours,
            [we.Hour(2020, 1, 1, 0), we.Hour(2020, 1, 1, 3)],
        ),
        (
            we.Minutes,
            [we.Minute(2020, 1, 1, 0, 0), we.Minute(2020, 1, 1, 0, 3)],
        ),
        (
            we.Seconds,
            [we.Second(2020, 1, 1, 0, 0, 0), we.Second(2020, 1, 1, 0, 0, 3)],
        ),
    ],
)  # type: ignore
def test_custom_intervals(
    intervals_type: Type[we.Intervals[we.Interval]],
    interval_values: list[we.Interval],
) -> None:
    assert len(interval_values) > 1
    intervals = intervals_type(interval_values)
    assert isinstance(intervals, intervals_type)
    assert isinstance(intervals, we.Intervals)

    # test __contains__
    for val in interval_values:
        assert val in intervals

    # test __iter__
    for val in intervals:
        assert val in interval_values

    # test __len__
    assert len(intervals) == len(interval_values)

    # test __getitem__
    for i, val in enumerate(interval_values):
        assert intervals[i] == val

    # test __eq__
    assert intervals == intervals_type(interval_values)
    with pytest.raises(NotImplementedError):
        assert intervals == object()

    # test __ne__
    assert intervals != intervals_type(interval_values[:-1])

    # test __repr__
    assert (
        repr(intervals)
        == intervals_type.__name__ + "([" + ", ".join(map(repr, interval_values)) + "])"
    )

    # test __str__
    assert str(intervals) == "{" + ", ".join(map(str, interval_values)) + "}"

    # # test __add__
    # assert intervals + intervals == intervals_type(interval_values + interval_values)

    # # test __sub__
    # assert intervals - intervals == intervals_type([])

    # # test __and__
    # assert intervals & intervals == intervals

    # # test __or__
    # assert intervals | intervals == intervals

    # # test __xor__
    # assert intervals ^ intervals == intervals_type([])
