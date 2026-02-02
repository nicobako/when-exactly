# When-Exactly

An expressive and intuitive library for working with dates.

## Rationale

When-Exactly is a library that aims to bring more human-friendly date-time types into the hands of developers,
so they can write more expressive code when working with dates.

## Overview

```python
>>> import when_exactly as wnx

>>> year = wnx.Year(2025) # the year 2025
>>> year
Year(2025)

>>> month = year.month(1) # month 1 (January) of the year
>>> month
Month(2025, 1)

>>> day = wnx.Day(2025, 12, 25) # December 25, 2025
>>> day
Day(2025, 12, 25)

>>> day.month # the month that the day is a part of
Month(2025, 12)

>>> day.week # the week that the day is a part of
Week(2025, 52)

>>> day.week.days[0:5] # all weekday (Mon thru Fri) of the week
Days([Day(2025, 12, 22), Day(2025, 12, 23), Day(2025, 12, 24), Day(2025, 12, 25), Day(2025, 12, 26)])

```
