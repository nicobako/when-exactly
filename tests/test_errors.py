import pytest

import when_exactly as we


def test_invalid_moment() -> None:
    msg = "Invalid moment: day is out of range for month"
    exc = we.InvalidMomentError(msg)
    assert isinstance(exc, RuntimeError)
    assert str(exc) == msg
