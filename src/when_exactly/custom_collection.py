from when_exactly.collection import Collection
from when_exactly.custom_interval import CustomInterval


class CustomCollection[T: CustomInterval](Collection[T]):
    pass
