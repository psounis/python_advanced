from functools import reduce

# sum
print(reduce(lambda x, y: x+y, [1,2,3,4]))

# max
print(reduce(lambda x, y: x if x>y else y, [1,2,3,4]))

# sum of squares
print(reduce(lambda x, y: x + y*y, [1,2,3,4], 0))