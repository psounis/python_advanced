from heapq import heapify, heappush, heappop
from random import randrange

array = [randrange(20) for i in range(10)]
print(array)
heapify(array)
print(array)

heappush(array, randrange(20))
heappush(array, randrange(20))
print("="*40)
while len(array)>0:
    item = heappop(array)
    print(f"{item}, {array}")
