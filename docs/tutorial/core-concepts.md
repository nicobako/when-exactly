# Core Concepts

Since _When-Exactly_ allows developers to interact with dates and times in a very unique way,
it is worth while becoming familiar with some of the lower-level building blocks.

## Moment

The [`Moment`](moment.md) represents, _a moment in time_. This is analogous to Python's
[datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) class.


!!!note
    The resolution of a moment is limited to _a second_.
    If you need more resolution, then when-exactly is probably not the library you need.

## Delta

The [`Delta`](delta.md) is analogous to Python's
[`datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta),
with extra functionality for deltas of _months_ and _years_.

## Interval

An _interval_ represents a _time span_.

```python
>>> interval = we.Interval(
...     start=we.Moment(2025, 2, 14, 12, 0, 0,),
...     stop=we.Moment(2025, 2, 14, 12, 30, 0),
... )
>>> str(interval)
'2025-02-14T12:00:00/2025-02-14T12:30:00'

```

This is the building block of all the _custom intervals_ like _Year_, _Month_, etc.

### Intervals

_Intervals_ (note that this word is plural)
represents a _collection of `Interval` objects_.


