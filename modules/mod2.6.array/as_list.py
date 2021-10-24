from array import array
from random import randrange

arr = array('i', (randrange(100) for _ in range(10)))

print(arr)
arr.append(12)
print(arr)
arr.remove(12)
print(arr)
elem = arr.pop()
print(elem, arr)
# arr.clear() doesn't work
print(arr)

