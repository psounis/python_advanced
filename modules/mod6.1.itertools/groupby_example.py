from random import randrange
from itertools import groupby

numbers = [randrange(2) for i in range(10)]
print(numbers)
print(list(groupby(numbers)))
for k, items in groupby(numbers):
    print("Key: " + str(k), end=". Items: ")
    for item in items:
        print(item, end=" ")
    print()

print("="*30)
numbers = [randrange(10) for i in range(20)]
print(numbers)
for k, items in groupby(numbers, lambda x: "even" if x%2==0 else "odd"):
    print("Key: " + str(k), end=". Items: ")
    for item in items:
        print(item, end=" ")
    print()

