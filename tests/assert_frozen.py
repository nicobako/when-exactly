import dataclasses
from typing import Any

import pytest


def assert_frozen(obj: Any) -> None:
    assert dataclasses.is_dataclass(obj)
    for field in obj.__dataclass_fields__.values():
        with pytest.raises(dataclasses.FrozenInstanceError):
            setattr(obj, field.name, "anything")
