from typing import Type

import pytest

import when_exactly as we


@pytest.mark.parametrize(
    [
        "intervals_type",
        "interval_values",
        "type_name",
    ],
    [
        (
            we.Years,
            [we.Year(2020), we.Year(2023)],
            "Years",
        ),
        (
            we.Months,
            [we.Month(2020, 1), we.Month(2020, 3)],
            "Months",
        ),
        (
            we.Weeks,
            [we.Week(2020, 1), we.Week(2020, 3)],
            "Weeks",
        ),
        (
            we.Days,
            [we.Day(2020, 1, 1), we.Day(2020, 1, 3)],
            "Days",
        ),
        (
            we.Hours,
            [we.Hour(2020, 1, 1, 0), we.Hour(2020, 1, 1, 3)],
            "Hours",
        ),
        (
            we.Minutes,
            [we.Minute(2020, 1, 1, 0, 0), we.Minute(2020, 1, 1, 0, 3)],
            "Minutes",
        ),
        (
            we.Seconds,
            [we.Second(2020, 1, 1, 0, 0, 0), we.Second(2020, 1, 1, 0, 0, 3)],
            "Seconds",
        ),
    ],
)  # type: ignore
def test_custom_intervals(
    intervals_type: Type[we.Collection[we.Interval]],
    interval_values: list[we.Interval],
    type_name: str,
) -> None:
    assert len(interval_values) > 1
    intervals = intervals_type(interval_values)
    assert isinstance(intervals, intervals_type)
    assert isinstance(intervals, we.Collection)

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
        == type_name + "([" + ", ".join(map(repr, interval_values)) + "])"
    )

    # test __str__
    assert str(intervals) == "{" + ", ".join(map(str, interval_values)) + "}"

    # test __getitem__ with slice
    intervals_slice = intervals[1:]
    assert isinstance(intervals_slice, intervals_type)
    assert intervals_slice.__class__.__name__ == type_name
    assert type_name in repr(intervals_slice)

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
