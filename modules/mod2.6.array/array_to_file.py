from array import array
from random import randrange

arr = array('i', (randrange(100) for _ in range(10**6)))
some_data = arr[:100]
print(some_data)

with open("data.bin", "wb") as f:
    arr.tofile(f)

with open("data.bin", "rb") as f:
    arr.fromfile(f, 10**6)
some_data = arr[:100]
print(some_data)

