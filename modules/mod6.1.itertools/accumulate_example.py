from itertools import accumulate

numbers = [1,2,3,4,5]
print(list(accumulate(numbers)))

it = accumulate(numbers, lambda x,y: x*y)
print(list(it))