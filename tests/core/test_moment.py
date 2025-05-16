import datetime

import pytest

import when_exactly as we
from tests.core.assert_frozen import assert_frozen


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


def test_add_delta() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)

    assert moment + we.Delta() == moment

    assert moment + we.Delta(seconds=1) == we.Moment(2020, 1, 1, 0, 0, 1)
    assert moment + we.Delta(seconds=-1) == we.Moment(2019, 12, 31, 23, 59, 59)
    assert moment + we.Delta(seconds=100) == we.Moment(2020, 1, 1, 0, 1, 40)
    assert moment + we.Delta(seconds=-100) == we.Moment(2019, 12, 31, 23, 58, 20)

    assert moment + we.Delta(minutes=1) == we.Moment(2020, 1, 1, 0, 1, 0)
    assert moment + we.Delta(minutes=-1) == we.Moment(2019, 12, 31, 23, 59, 0)
    assert moment + we.Delta(minutes=100) == we.Moment(2020, 1, 1, 1, 40, 0)
    assert moment + we.Delta(minutes=-100) == we.Moment(2019, 12, 31, 22, 20, 0)

    assert moment + we.Delta(hours=1) == we.Moment(2020, 1, 1, 1, 0, 0)
    assert moment + we.Delta(hours=-1) == we.Moment(2019, 12, 31, 23, 0, 0)
    assert moment + we.Delta(hours=100) == we.Moment(2020, 1, 5, 4, 0, 0)
    assert moment + we.Delta(hours=-100) == we.Moment(2019, 12, 27, 20, 0, 0)

    assert moment + we.Delta(days=1) == we.Moment(2020, 1, 2, 0, 0, 0)
    assert moment + we.Delta(days=-1) == we.Moment(2019, 12, 31, 0, 0, 0)
    assert moment + we.Delta(days=100) == we.Moment(2020, 4, 10, 0, 0, 0)
    assert moment + we.Delta(days=-100) == we.Moment(2019, 9, 23, 0, 0, 0)
    assert moment + we.Delta(days=1000) == we.Moment(2022, 9, 27, 0, 0, 0)
    assert moment + we.Delta(days=-1000) == we.Moment(2017, 4, 6, 0, 0, 0)

    assert moment + we.Delta(weeks=1) == we.Moment(2020, 1, 8, 0, 0, 0)
    assert moment + we.Delta(weeks=-1) == we.Moment(2019, 12, 25, 0, 0, 0)
    assert moment + we.Delta(weeks=100) == we.Moment(2021, 12, 1, 0, 0, 0)
    assert moment + we.Delta(weeks=-100) == we.Moment(2018, 1, 31, 0, 0, 0)

    assert moment + we.Delta(months=1) == we.Moment(2020, 2, 1, 0, 0, 0)
    assert moment + we.Delta(months=-1) == we.Moment(2019, 12, 1, 0, 0, 0)
    assert moment + we.Delta(months=12) == we.Moment(2021, 1, 1, 0, 0, 0)
    assert moment + we.Delta(months=-12) == we.Moment(2019, 1, 1, 0, 0, 0)


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
