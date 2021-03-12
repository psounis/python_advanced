from datetime import date

date1 = date(2021, 11, 21)
print(date1)

date2 = date.today()
print(date2)
print(f"{date2.day}/{date2.month}/{date2.year}")

date3 = date.fromisoformat('2021-11-21')
print(date3)

