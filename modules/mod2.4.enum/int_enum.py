from enum import IntEnum


class Days(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

week_jobs = ["some", "more work", "much more work"]

print(week_jobs[Days.MONDAY])
print(week_jobs[Days.TUESDAY])