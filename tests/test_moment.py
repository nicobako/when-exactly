import datetime

import pytest
from assert_frozen import assert_frozen

import when_exactly as we


def test_moment() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    assert str(moment) == "2020-1-1 0:0:0"
    assert moment.year == 2020
    assert moment.month == 1
    assert moment.day == 1
    assert moment.hour == 0
    assert moment.minute == 0
    assert moment.second == 0
    assert moment == we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment != we.Moment(2020, 1, 1, 0, 0, 1)
    assert_frozen(moment)


def test_moment_to_datetime() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    dt = moment.to_datetime()
    assert dt == datetime.datetime(2020, 1, 1, 0, 0, 0)
    assert dt.microsecond == 0


def test_moment_from_datetime() -> None:
    dt = datetime.datetime(2020, 1, 1, 0, 0, 0)
    moment = we.Moment.from_datetime(dt)
    assert moment == we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment.to_datetime() == dt


def test_invalid_moments_raise() -> None:
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


def test_next_month() -> None:
    moment = we.Moment(2020, 1, 1, 0, 0, 0)
    assert moment.next_month() == we.Moment(2020, 2, 1, 0, 0, 0)

    moment = we.Moment(2020, 12, 1, 0, 0, 0)
    assert moment.next_month() == we.Moment(2021, 1, 1, 0, 0, 0)
