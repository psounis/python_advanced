# functions from the official docs: https://docs.python.org/3/library/bisect.html
from random import randrange
from bisect import bisect_left, bisect_right

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


numbers = [randrange(10) for _ in range(10)] + [5, 5]
numbers.sort()

print(numbers)
print(index(numbers, 5))
print(find_lt(numbers, 5))
print(find_le(numbers, 5))
print(find_gt(numbers, 5))
print(find_ge(numbers, 5))