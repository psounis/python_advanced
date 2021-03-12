from datetime import datetime, timedelta

d = datetime(2021, 11, 1, 13, 11, 39)
print(d.isoformat(sep=" "))
print(d, d + timedelta(hours=48))
print(d.replace(hour=23))

print(d < datetime(2022, 1, 1))
print(d == datetime(2021, 11, 1))