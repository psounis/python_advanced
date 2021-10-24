from array import array
from random import randrange

arr = array('i', (randrange(100) for _ in range(50)))

print("initial array: " + str(arr))

l = arr.tolist()
print("as list: " + str(l))

bytes = arr.tobytes()
print("as bytes: " + str(bytes))

reconstructed = array('i')
arr.frombytes(bytes)
print("reconstructed: " + str(arr))