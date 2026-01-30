# Moment

The `Moment` represents _a moment in time_. It is analogous to Python's
[datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) class.

The `Moment` is a simple class that it is used prevalently throughout _When-Exactly_.

## Creating a Moment

```python
>>> import when_exactly as wnx

>>> moment = wnx.Moment(
...     year=2025,
...     month=1,
...     day=30,
...     hour=15,
...     minute=25,
...     second=30,
... )
>>> moment
Moment(year=2025, month=1, day=30, hour=15, minute=25, second=30)

>>> # or, more concisely 
>>> wnx.Moment(year=2025, month=1, day=30, hour=15, minute=25, second=30)
Moment(year=2025, month=1, day=30, hour=15, minute=25, second=30)

```

Moments can be created from datetimes, and can be converted to datetimes.

```python
>>> import datetime

>>> moment.to_datetime()
datetime.datetime(2025, 1, 30, 15, 25, 30)

>>> dt = datetime.datetime(2025, 1, 30, 15, 25, 30)
>>> wnx.Moment.from_datetime(dt)
Moment(year=2025, month=1, day=30, hour=15, minute=25, second=30)

```

## Moment Validation

A `Moment` is always a valid date-time.

```python
>>> wnx.Moment(2025, 1, 32, 0,0,0)
Traceback (most recent call last):
    ...
when_exactly.core.errors.InvalidMomentError: Invalid Moment: day 32 must be in range 1..31 for month 1 in year 2025

```

## Comaring Moments

`Moment`s can be compared to one another

```python
>>> moment1 = wnx.Moment(2025, 1, 1, 0, 0, 0)
>>> moment2 = wnx.Moment(2025, 1, 1, 1, 0, 0)
>>> assert moment1 != moment2
>>> assert moment1 < moment2
>>> assert moment1 <= moment2
>>> assert moment2 > moment1
>>> assert moment2 >= moment1
>>> assert moment1 == wnx.Moment(2025, 1, 1, 0, 0, 0)

```

## Adding Deltas to Moments

A [`Delta`](./delta.md) can be added to a `Moment`.

```python
>>> moment = wnx.Moment(2025, 1, 31, 12, 30, 30)
>>> moment + wnx.Delta(years=1)
Moment(year=2026, month=1, day=31, hour=12, minute=30, second=30)

>>> moment + wnx.Delta(months=1)
Moment(year=2025, month=2, day=28, hour=12, minute=30, second=30)

>>> moment + wnx.Delta(days=2)
Moment(year=2025, month=2, day=2, hour=12, minute=30, second=30)

>>> # etc.

```

## Weeks

A moment's ISO year, week, and weekday are accessible as follows:

```python
>>> # 2019-12-31 == 2020-W01-2
>>> moment = wnx.Moment(2019, 12, 31, 0,0,0)

>>> moment.week_year
2020

>>> moment.week
1

>>> moment.week_day
2

```

## API Reference

For complete API documentation including all methods and properties, see the [Moment API Reference](api.md#moment).
