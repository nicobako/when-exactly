import pytest

import when_exactly as we


@pytest.mark.parametrize(
    "precision, expected_precision",
    [
        (we.Precisions.SECOND, we.Precision(1, "second", we.Delta(seconds=1))),
        (we.Precisions.MINUTE, we.Precision(2, "minute", we.Delta(minutes=1))),
        (we.Precisions.HOUR, we.Precision(3, "hour", we.Delta(hours=1))),
        (we.Precisions.DAY, we.Precision(4, "day", we.Delta(days=1))),
        (we.Precisions.WEEK, we.Precision(5, "week", we.Delta(weeks=1))),
        (we.Precisions.MONTH, we.Precision(6, "month", we.Delta(months=1))),
        (we.Precisions.YEAR, we.Precision(7, "year", we.Delta(years=1))),
    ],
)
def test_precision(precision: we.Precisions, expected_precision: we.Precision) -> None:
    assert precision.value == expected_precision
