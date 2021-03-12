from datetime import date

d = date(1990,11,1)
print(d.isoformat(), d)

d2 = d.replace(day=12)
print(d2)
print(f"Weekday: {d2.weekday()}")

print(d < d2)
print(d > d2)