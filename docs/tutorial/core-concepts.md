# Core Concepts

Since _When-Exactly_ allows developers to interact with dates and times in a very unique way,
it is worth while becoming familiar with some of the lower-level building blocks.

## Moment

The `Moment` represents, as the name suggests, _a moment in time_. This is analogous to Python's
[datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) class.

```python
>>> import when_exactly as we

>>> moment = we.Moment(
...     year=2025,
...     month=1,
...     day=30,
...     hour=15,
...     minute=25,
...     second=30,
... )
>>> moment
Moment(year=2025, month=1, day=30, hour=15, minute=25, second=30)

```

Moments can be created from datetimes, and can be converted to datetimes.

```python
>>> import datetime

>>> moment.to_datetime()
datetime.datetime(2025, 1, 30, 15, 25, 30)

>>> dt = datetime.datetime(2025, 1, 30, 15, 25, 30)
>>> we.Moment.from_datetime(dt)
Moment(year=2025, month=1, day=30, hour=15, minute=25, second=30)

```


The `Moment` is really a simple class, but it is used prevalently throughought _When-Exactly_.





