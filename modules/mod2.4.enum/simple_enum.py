from enum import Enum


class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today = Days.MONDAY
print(today)
print(today.name)
print(today.value)
print(type(today))
print(isinstance(today, Days))