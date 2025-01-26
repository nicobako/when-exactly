# Welcome to when-exactly

An expressive and intuitive library for working with dates.

## Rationale

When we think about dates and times, we think in terms of _years_, _months_, _weeks_, _days_, _hours_, _minutes_, etc.

When-Exactly is a library that aims to bring these types into the hands of developers,
so they can write more expressive code when working with dates.

## Overview

```python
>>> import when_exactly as we

>>> year = we.Year(2025)
>>> year
Year(2025)

>>> month = year.month(1)
>>> month
Month(2025, 1)

>>> day = we.Day(2025, 12, 25)
>>> day
Day(2025, 12, 25)

>>> day.month()
Month(2025, 12)

```