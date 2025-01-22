import dataclasses

from when_exactly.interval import Interval
from when_exactly.moment import Moment


@dataclasses.dataclass(frozen=True)
class Year(Interval):
    pass

    def month(self, month: int) -> None:
        pass
        # return Month(
        #     start=Moment(self.start.year, month, 1, 0, 0, 0),
        #     stop=Moment(
        #         self.start.year if month < 12 else self.start.year + 1,
        #         month + 1 if month < 12 else 1,
        #         1,
        #         0,
        #         0,
        #         0,
        #     ),
        # )


def year(year: int) -> Year:
    return Year(
        start=Moment(year, 1, 1, 0, 0, 0),
        stop=Moment(year + 1, 1, 1, 0, 0, 0),
    )
