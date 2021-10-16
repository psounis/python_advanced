from random import randrange
from bisect import bisect, insort

numbers = [randrange(100) for _ in range(20)]
numbers.sort(key=lambda x: x // 10 + x % 10)
keys = [x // 10 + x % 10 for x in numbers]
print(numbers)
print(keys)

new_value = 25
key = new_value // 10 + new_value % 10
pos = bisect(keys, key)
insort(keys, key)
numbers.insert(pos, new_value)
print(numbers)
print(keys)
