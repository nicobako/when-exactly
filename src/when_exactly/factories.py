from when_exactly.moment import Moment
import datetime

def now()->Moment:
    return Moment.from_datetime(datetime.datetime.now())