from operator import add
from functools import reduce
from random import randrange

my_list = [randrange(10) for _ in range(10)]
print(my_list)


def my_add(a, b):
    return a+b


print(reduce(my_add, my_list, 0))
print(reduce(add, my_list, 0))
print(reduce(lambda x, y: x+y, my_list, 0))