# API Reference

Comprehensive API documentation for all when-exactly classes.

## Core Concepts

The foundational building blocks of when-exactly:

- **[Moment](api/moment.md)** - A precise point in time
- **[Delta](api/delta.md)** - A time difference for arithmetic operations
- **[Interval](api/interval.md)** - A continuous span of time between two moments
- **[Collection](api/collection.md)** - A sorted, deduplicated collection of intervals
- **[Custom Interval](api/custom-interval.md)** - A base class for defining custom intervals

## Intervals

Time intervals representing specific durations:

- **[Year](api/year.md)** - A calendar year (365 or 366 days)
- **[Month](api/month.md)** - A calendar month (28-31 days)
- **[Week](api/week.md)** - An ISO week (7 days)
- **[Day](api/day.md)** - A 24-hour day using Gregorian calendar coordinates
- **[OrdinalDay](api/ordinal-day.md)** - A 24-hour day using ordinal day-of-year numbering (1-366)
- **[Weekday](api/weekday.md)** - A 24-hour day within an ISO week (1=Monday, 7=Sunday)
- **[Hour](api/hour.md)** - A 60-minute hour
- **[Minute](api/minute.md)** - A 60-second minute
- **[Second](api/second.md)** - A 1-second interval

## Collections

Collections of intervals with additional functionality:

- **[Years](api/years.md)** - Collection of Year intervals
- **[Months](api/months.md)** - Collection of Month intervals
- **[Weeks](api/weeks.md)** - Collection of Week intervals
- **[Days](api/days.md)** - Collection of Day intervals (with `.months` property)
- **[Weekdays](api/weekdays.md)** - Collection of Weekday intervals
- **[Hours](api/hours.md)** - Collection of Hour intervals
- **[Minutes](api/minutes.md)** - Collection of Minute intervals
- **[Seconds](api/seconds.md)** - Collection of Second intervals
