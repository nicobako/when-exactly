import datetime

from when_exactly.moment import Moment


def now() -> Moment:
    return Moment.from_datetime(datetime.datetime.now())
