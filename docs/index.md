# Welcome to when-exactly

Because you should be able to work with time the same way you think about time.

## Rationale

There are many libraries available for working with dates and times, but the majority of them provide functionality for working with the same basic units of time: _dates, times, and datetimes_.

We tink about dates and times throughout the day, but we often don't think in _datetimes_; we think in _years_, _months_, _weeks_, _days_, _hours_, _minutes_, etc.

The world needs a library that provides functionality for working with time in the same way that we think about time.

## Overview

```python
>>> import when_exactly as we
>>> year = we.year(2025)
>>> year.iso()
'2025'

>>> month = year.month(1)
>>> month.iso()
'2025-01'

```