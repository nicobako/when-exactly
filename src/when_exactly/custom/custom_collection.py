from when_exactly.core.collection import Collection
from when_exactly.custom.custom_interval import CustomInterval


class CustomCollection[T: CustomInterval](Collection[T]):
    pass
