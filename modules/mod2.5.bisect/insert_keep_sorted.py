from random import randrange
from bisect import insort

numbers = [0]
for i in range(1, 30):
    numbers.append(numbers[i-1] + randrange(2))
print(numbers)

insort(numbers, 5)
print(numbers)
insort(numbers, 7)
print(numbers)