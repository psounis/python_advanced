import functools
from enum import Enum


class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    def mood(self):
        if self.value <= 5:
            return "bad"
        else:
            return "good"

    @classmethod
    def best_day(cls):
        return cls.SUNDAY


for day in Days:
    print(day, day.mood())

print(Days.best_day())