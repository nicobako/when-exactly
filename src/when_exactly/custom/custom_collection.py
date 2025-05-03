from typing import Generic, TypeVar

from when_exactly.core.collection import Collection
from when_exactly.custom.custom_interval import CustomInterval

CustomIntervalType = TypeVar("CustomIntervalType", bound=CustomInterval)


class CustomCollection(Generic[CustomIntervalType], Collection[CustomIntervalType]):
    pass
