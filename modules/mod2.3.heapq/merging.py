from heapq import merge
from random import randrange


data1 = [randrange(20) for _ in range(10)]
data2 = [randrange(20) for _ in range(10)]
data3 = [randrange(20) for _ in range(10)]

data1.sort()
data2.sort()
data3.sort()

print(data1)
print(data2)
print(data3)
print(list(merge(data1, data2, data3)))

data1.sort(key=lambda x:x%3)
data2.sort(key=lambda x:x%3)
data3.sort(key=lambda x:x%3)

print(data1)
print(data2)
print(data3)
print(list(merge(data1, data2, data3, key=lambda x:x%3)))
