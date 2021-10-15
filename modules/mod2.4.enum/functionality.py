from enum import Enum

class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


print("="*30)
# iterable
for day in Days:
    print(day)

print("="*30)
# hashable
workload = {Days.MONDAY: "a lot",
            Days.TUESDAY: "a little",
            Days.SUNDAY: "nothing"}
print(workload)

print("="*30)
# get an enum member
print(Days.WEDNESDAY) # usual way
print(Days["WEDNESDAY"]) # by member name
print(Days(3)) # by member value

print("="*30)
# comparisons
print(Days.MONDAY==Days.MONDAY)
print(Days.MONDAY!=Days.TUESDAY)
try:
    print(Days.MONDAY<Days.TUESDAY)
except TypeError:
    print("can't compare them")