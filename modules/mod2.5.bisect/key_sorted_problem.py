from random import randrange
from bisect import insort

numbers = [randrange(100) for _ in range(20)]
print(numbers)

numbers.sort(key=lambda x: x//10+x%10)
print(numbers)

insort(numbers, 45)
print(numbers)