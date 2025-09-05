import dataclasses
from typing import Any, Type

import pytest

import when_exactly as we


@dataclasses.dataclass
class CustomIntervalParams:
    custom_interval_type: Type[we.CustomInterval]
    custom_interval: we.CustomInterval
    expected_start: we.Moment
    expected_stop: we.Moment
    expected_repr: str
    expected_str: str
    expected_next: we.CustomInterval
    expected_prev: we.CustomInterval


def assert_custom_interval_implemented_correctly(
    params: CustomIntervalParams,
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

    assert params.custom_interval + 1 == params.expected_next
    assert params.custom_interval - 1 == params.expected_prev

    assert params.custom_interval + 0 == params.custom_interval
    assert params.custom_interval - 0 == params.custom_interval

    assert params.custom_interval + 2 == params.expected_next.next
    assert params.custom_interval - 2 == params.expected_prev.previous


def assert_frozen(obj: Any) -> None:
    assert dataclasses.is_dataclass(obj)
    for field in obj.__dataclass_fields__.values():
        with pytest.raises(dataclasses.FrozenInstanceError):
            setattr(obj, field.name, "anything")


@dataclasses.dataclass
class CustomCollectionParams[T: we.CustomInterval]:
    collection_type: Type[we.CustomCollection[T]]
    interval_values: list[T]
    type_name: str


def assert_custom_collection_implemented_correctly[T: we.CustomInterval](
    params: CustomCollectionParams[T],
) -> None:
    interval_values = params.interval_values
    collection_type = params.collection_type
    type_name = params.type_name

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
