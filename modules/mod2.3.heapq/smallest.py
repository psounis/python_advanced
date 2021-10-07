from heapq import heapify, nsmallest
from random import randrange


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return self.name + "(" + str(self.age) + ")"


array = [Person("name", randrange(20)) for i in range(10)]
print(*array)
heapify(array)
print(*array)

ml = nsmallest(4, array)
print(*ml)

ml = nsmallest(4, array, lambda person: 20-person.age)
print(*ml)

print(*array)