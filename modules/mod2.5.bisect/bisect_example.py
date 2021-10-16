from random import randrange
from bisect import bisect

numbers = [0]
for i in range(1, 30):
    numbers.append(numbers[i-1] + randrange(2))
print(numbers)


print(bisect(numbers, 10))
print(bisect(numbers, 10, 5, 10))