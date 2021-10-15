from enum import Enum

Days = Enum("Days", "MONDAY TUESDAY WEDNESDAY THURSDAY " +
                    "FRIDAY SATURDAY SUNDAY")

for day in Days:
    print(day.name, day.value)