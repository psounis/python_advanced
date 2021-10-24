from array import array
from random import randrange

arr = array('i', (randrange(100) for _ in range(1000)))

print(arr)

element = 12
occurrences = arr.count(element)
print("occurrences=" + str(occurrences))
pos = 0
for _ in range(occurrences):
    pos = arr.index(element, pos)
    print("pos = " + str(pos))
    pos = pos + 1