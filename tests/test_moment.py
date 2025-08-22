import datetime
import itertools

import pytest

import when_exactly as we
from tests.asserts import assert_frozen


def test_initialization() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    assert_frozen(moment)
    assert moment.year == 2020
    assert moment.month == 1
    assert moment.day == 1
    assert moment.hour == 0
    assert moment.minute == 0
    assert moment.second == 0
    assert moment == we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment != we.Moment(2020, 1, 1, 0, 0, 1)


def test_to_datetime() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    dt = moment.to_datetime()
    assert dt == datetime.datetime(2020, 1, 1, 0, 0, 0)
    assert dt.microsecond == 0


def test_from_datetime() -> None:
    dt = datetime.datetime(2020, 1, 1, 0, 0, 0)
    moment = we.Moment.from_datetime(dt)
    assert moment == we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment.to_datetime() == dt


def test_invalid_datetime_raise() -> None:
    invalid_args = [2020, 1, 44, 0, 0, 0]
    with pytest.raises(ValueError):
        we.Moment(*invalid_args)


def test_comparators() -> None:
    moment_args = [2020, 2, 2, 1, 1, 1]
    moment1 = we.Moment(*moment_args)
    eq_args = moment_args.copy()
    moment_eq = we.Moment(*eq_args)
    assert moment1 == moment_eq
    for i in range(len(moment_args)):
        lt_args = moment_args.copy()
        lt_args[i] = lt_args[i] - 1
        moment_lt = we.Moment(*lt_args)
        assert moment_lt < moment1
        assert moment_lt <= moment1
        assert moment_eq <= moment1
        gt_args = moment_args.copy()
        gt_args[i] = gt_args[i] + 1
        moment_gt = we.Moment(*gt_args)
        assert moment_gt > moment1
        assert moment_gt >= moment1
        assert moment_eq >= moment1


@pytest.mark.parametrize(
    "delta_type, delta_value, expected_plus, expected_minus",
    [
        (
            "seconds",
            1,
            we.Moment(2020, 1, 1, 0, 0, 1),
            we.Moment(2019, 12, 31, 23, 59, 59),
        ),
        (
            "seconds",
            100,
            we.Moment(2020, 1, 1, 0, 1, 40),
            we.Moment(2019, 12, 31, 23, 58, 20),
        ),
        (
            "minutes",
            1,
            we.Moment(2020, 1, 1, 0, 1, 0),
            we.Moment(2019, 12, 31, 23, 59, 0),
        ),
        (
            "minutes",
            100,
            we.Moment(2020, 1, 1, 1, 40, 0),
            we.Moment(2019, 12, 31, 22, 20, 0),
        ),
        ("hours", 1, we.Moment(2020, 1, 1, 1, 0, 0), we.Moment(2019, 12, 31, 23, 0, 0)),
        (
            "hours",
            100,
            we.Moment(2020, 1, 5, 4, 0, 0),
            we.Moment(2019, 12, 27, 20, 0, 0),
        ),
        ("days", 1, we.Moment(2020, 1, 2, 0, 0, 0), we.Moment(2019, 12, 31, 0, 0, 0)),
        ("days", 100, we.Moment(2020, 4, 10, 0, 0, 0), we.Moment(2019, 9, 23, 0, 0, 0)),
        ("days", 1000, we.Moment(2022, 9, 27, 0, 0, 0), we.Moment(2017, 4, 6, 0, 0, 0)),
        ("weeks", 1, we.Moment(2020, 1, 8, 0, 0, 0), we.Moment(2019, 12, 25, 0, 0, 0)),
        (
            "weeks",
            100,
            we.Moment(2021, 12, 1, 0, 0, 0),
            we.Moment(2018, 1, 31, 0, 0, 0),
        ),
        ("months", 1, we.Moment(2020, 2, 1, 0, 0, 0), we.Moment(2019, 12, 1, 0, 0, 0)),
        ("months", 12, we.Moment(2021, 1, 1, 0, 0, 0), we.Moment(2019, 1, 1, 0, 0, 0)),
    ],
)
def test_add_delta_parametrized(
    delta_type: str,
    delta_value: int,
    expected_plus: we.Moment,
    expected_minus: we.Moment,
) -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    delta_kwargs = {delta_type: delta_value}
    delta = we.Delta(**delta_kwargs)
    delta_neg = we.Delta(**{delta_type: -delta_value})

    assert moment + delta == expected_plus
    assert moment + delta_neg == expected_minus
    assert moment - delta == expected_minus
    assert moment - delta_neg == expected_plus


@pytest.mark.parametrize(
    "delta_type", ["seconds", "minutes", "hours", "days", "weeks", "months"]
)
def test_add_delta_zero(delta_type: str) -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    delta = we.Delta(**{delta_type: 0})
    assert moment + delta == moment


def test_add_delta_edge_cases() -> None:
    leap_year = we.Moment(2020, 2, 29, 0, 0, 0)
    assert leap_year + we.Delta(days=1) == we.Moment(2020, 3, 1, 0, 0, 0)
    assert leap_year + we.Delta(days=-1) == we.Moment(2020, 2, 28, 0, 0, 0)
    assert leap_year + we.Delta(days=365) == we.Moment(2021, 2, 28, 0, 0, 0)
    assert we.Moment(2020, 3, 31, 0, 0, 0) + we.Delta(months=-1) == we.Moment(
        2020, 2, 29, 0, 0, 0
    )
    assert leap_year + we.Delta(years=1) == we.Moment(2021, 2, 28, 0, 0, 0)


def test_moment_week_accessors() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment.week_year == 2020
    assert moment.week == 1
    assert moment.week_day == 3

    moment = we.Moment(2020, 12, 31, 0, 0, 0)
    assert moment.week_year == 2020
    assert moment.week == 53
    assert moment.week_day == 4

    moment = we.Moment(2019, 12, 31, 0, 0, 0)
    assert moment.week_year == 2020
    assert moment.week == 1
    assert moment.week_day == 2


def test_moment_ordinal_accessors() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment.ordinal_day == 1

    moment = we.Moment(2020, 12, 31, 0, 0, 0)
    assert moment.ordinal_day == 366

    moment = we.Moment(2019, 12, 31, 0, 0, 0)
    assert moment.ordinal_day == 365


@pytest.mark.parametrize(
    ["year", "month", "day", "hour", "minute", "second"],
    [
        (datetime.MAXYEAR + 100, 1, 1, 1, 1, 1),
        (2020, 1, 32, 1, 1, 1),  # day
        (2020, 13, 1, 1, 1, 1),  # month
        (2020, 1, 1, 40, 1, 1),  # hour
        (2020, 1, 1, 1, 80, 1),  # minute
        (2020, 1, 1, 1, 1, 100),  # second
    ],
)
def test_moment_invalid(
    year: int, month: int, day: int, hour: int, minute: int, second: int
) -> None:
    try:
        datetime.datetime(
            year=year, month=month, day=day, hour=hour, minute=minute, second=second
        )
    except ValueError as e:
        message = str(e)
    else:
        raise RuntimeError("Expected ValueError not raised")
    with pytest.raises(we.InvalidMomentError, match=f"Invalid Moment: {message}"):
        we.Moment(
            year=year, month=month, day=day, hour=hour, minute=minute, second=second
        )
