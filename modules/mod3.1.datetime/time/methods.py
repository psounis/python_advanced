from datetime import time, timedelta

t1 = time.fromisoformat('11:12:13')
t2 = t1.replace(hour=23, second=11)
print(t1, t2)
print(t1 < t2)
print(t1 > t2)
