# Core Concepts

_When-Exactly_ is basically a wrapper around Python's already awesome [`datetime`][datetime] module, and allows developers to work with dates in a more abstract way.

## Moment

The [`Moment`][moment] represents, _a moment in time_. This is analogous to Python's
[`datetime.datetime`][datetime.datetime] class.

!!! note
The resolution of a moment is limited to _a second_.
If you need more resolution, then when-exactly is probably not the library you need.

```python
>>> moment = we.Moment(
...     year=2025,
...     month=3,
...     day=14,
...     hour=15,
...     minute=0,
...     second=0,
... )
>>> str(moment)
'2025-03-14T15:00:00'

```

## Delta

The [`Delta`](../tutorial/delta.md) is analogous to Python's
[`datetime.timedelta`][datetime.timedelta],
with extra functionality for deltas of _years_ and _months_.

```python
>>> delta = we.Delta(
...    years=1,
...    months=1,
...    weeks=2,
... )
>>> moment + delta
Moment(year=2026, month=4, day=28, hour=15, minute=0, second=0)

```

## Interval

An [`Interval`][interval] represents a _time span_.
An _interval_ has an inclusive _start_ and an exclusive _stop_.

```python
>>> interval = we.Interval(
...     start=we.Moment(2025, 2, 14, 12, 0, 0,),
...     stop=we.Moment(2025, 2, 14, 12, 30, 0),
... )
>>> str(interval)
'2025-02-14T12:00:00/2025-02-14T12:30:00'

```

## Custom Interval

A [`CustomInterval`](../tutorial/custom-interval.md) represents a _time span with a specific resolution_.

This is the building block of all the _custom intervals_ like _Year_, _Month_, etc.

## Collection

The [`Collection`](../tutorial/collection.md) represents a _collection of `Interval` objects_.
It provides all of the standard functionality you would expect a container to have

```python
>>> collection = we.Collection([
...    we.Day(2023, 1, 5),
...    we.Day(2023, 1, 7),
...    we.Week(2023, 10),
... ])
>>> collection[0]
Day(2023, 1, 5)

>>> collection[0:2]
Collection([Day(2023, 1, 5), Day(2023, 1, 7)])

>>> we.Week(2023, 10) in collection
True

>>> for interval in collection:
...     print(interval)
2023-01-05
2023-01-07
2023-W10

```

<!-- Links -->

[datetime]: https://docs.python.org/3/library/datetime.html
[datetime.datetime]: https://docs.python.org/3/library/datetime.html#datetime.datetime
[datetime.timedelta]: https://docs.python.org/3/library/datetime.html#datetime.timedelta
[interval]: /interval
[moment]: /moment
