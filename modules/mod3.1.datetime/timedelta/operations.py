from datetime import date, timedelta

d = date(2021, 12, 31)
t = timedelta(days=10)
print(d+t)
d2 = d-t
print(repr(d2-d))
print(date.today()+timedelta(days=10000))
