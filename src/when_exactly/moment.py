import datetime
import dataclasses

@dataclasses.dataclass
class Moment:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"
    
    def to_datetime(self):
        return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)