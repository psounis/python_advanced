from itertools import count, cycle, repeat

it = (val for val in count(10,2))
print(next(it), next(it))

print("="*20)
it = (val for val in cycle([1,2,3,4]))
for i in range(10):
    print(next(it))

print("="*20)
for i in repeat(10,3):
    print(i, end=" ")
