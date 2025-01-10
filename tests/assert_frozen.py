import pytest
import dataclasses
from typing import Any

def assert_frozen(obj: Any):
    assert dataclasses.is_dataclass(obj)
    for field in obj.__dataclass_fields__.values():
        with pytest.raises(dataclasses.FrozenInstanceError):
            setattr(obj, field.name, "anything")
