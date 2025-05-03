from typing import Type

import pytest

import when_exactly as we


@pytest.mark.parametrize(
    [
        "collection_type",
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
def test_custom_collection(
    collection_type: Type[we.CustomCollection[we.CustomInterval]],
    interval_values: list[we.CustomInterval],
    type_name: str,
) -> None:
    assert len(interval_values) > 1
    collection = collection_type(interval_values)
    assert isinstance(collection, we.CustomCollection)
    assert isinstance(collection, collection_type)

    # test __contains__
    for val in interval_values:
        assert val in collection

    # test __iter__
    for val in collection:
        assert val in interval_values

    # test __len__
    assert len(collection) == len(interval_values)

    # test __eq__
    assert collection == collection_type(interval_values)
    with pytest.raises(NotImplementedError):
        assert collection == object()

    # test __ne__
    assert collection != collection_type(interval_values[:-1])

    # test __repr__
    assert (
        repr(collection)
        == type_name + "([" + ", ".join(map(repr, interval_values)) + "])"
    )

    # test __str__
    assert str(collection) == "{" + ", ".join(map(str, interval_values)) + "}"

    # test __getitem__ with int
    for i, val in enumerate(interval_values):
        assert collection[i] == val

    # test __getitem__ with slice
    collection_slice = collection[1:]
    assert isinstance(collection_slice, collection_type)
    assert collection_slice.__class__.__name__ == type_name
    assert type_name in repr(collection_slice)

    # # test __add__
    # assert collection + collection == collection_type(interval_values + interval_values)

    # # test __sub__
    # assert collection - collection == collection_type([])

    # # test __and__
    # assert collection & collection == collection

    # # test __or__
    # assert collection | collection == collection

    # # test __xor__
    # assert collection ^ collection == collection_type([])
