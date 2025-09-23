import pytest

import when_exactly as wnx


def test_invalid_moment() -> None:
    msg = "day is out of range for month"
    exc = wnx.InvalidMomentError(msg)
    assert isinstance(exc, RuntimeError)
    assert str(exc) == f"Invalid Moment: {msg}"
