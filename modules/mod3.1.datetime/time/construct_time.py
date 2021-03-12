from datetime import time

time1 = time(11, 14, 24)
print(time1)

time2 = time.fromisoformat('11:14:12')
print(time2.hour, time2.minute, time2.second)