from datetime import timedelta

t1 = timedelta(hours=5)
t2 = timedelta(days=10, hours=25, seconds=100)
print(t1+t2)
print(t1/5, t1/100000)
print(-t2)
