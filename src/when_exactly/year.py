import dataclasses

from when_exactly.interval import Interval
from when_exactly.moment import Moment


@dataclasses.dataclass(frozen=True)
class Year(Interval):
    pass


def year(year: int) -> Year:
    return Year(
        start=Moment(year, 1, 1, 0, 0, 0),
        stop=Moment(year + 1, 1, 1, 0, 0, 0),
    )
