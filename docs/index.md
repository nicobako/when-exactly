# When-Exactly

An expressive and intuitive library for working with dates.

## Rationale

When we, as _ordinary people_, talk about dates and times we use words like _months, weeks, days, years, etc._
Yet, when we, _as developers_, have to work with dates in code we are limited to concepts like _datetime, date, and time_.

When-Exactly is a library that aims to bring useful date and time abstractions into the hands of developers,
so they can write more expressive code.

## Overview

```python
>>> import when_exactly as we

>>> year = we.Year(2025) # the year 2025
>>> year
Year(2025)

>>> month = year.month(1) # month 1 (January) of the year
>>> month
Month(2025, 1)

>>> day = we.Day(2025, 12, 25) # December 25, 2025
>>> day
Day(2025, 12, 25)

>>> day.month # the month that the day is a part of
Month(2025, 12)

>>> day.week # the week that the day is a part of
Week(2025, 52)

```

::: when_exactly
    options:
        members: no
