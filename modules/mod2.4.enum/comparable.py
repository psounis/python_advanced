import functools
from enum import Enum


@functools.total_ordering
class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    def __gt__(self,other):
        return self.value > other.value


print(Days.MONDAY > Days.WEDNESDAY)
print(Days.MONDAY >= Days.WEDNESDAY)
print(Days.MONDAY < Days.WEDNESDAY)
print(Days.MONDAY <= Days.WEDNESDAY)