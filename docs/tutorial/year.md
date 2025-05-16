# Year

The `Year` represents an entire year, starting from _January 1_ to _December 31_.

## Creating a Year

```python
>>> import when_exactly as we

>>> year = we.Year(2025)
>>> year
Year(2025)

>>> str(year)
'2025'

```

## The Months of a Year

Get the [`Months`](months.md) of a year.

```python
>>> months = year.months
>>> len(months)
12

>>> months[0]
Month(2025, 1)

>>> months[-2:]
Months([Month(2025, 11), Month(2025, 12)])

```

## The Weeks of a Year

Get the [`Weeks`](weeks.md) of a year.

```python
>>> weeks = year.weeks
>>> len(weeks)
52

>>> weeks[0]
Week(2025, 1)

```
