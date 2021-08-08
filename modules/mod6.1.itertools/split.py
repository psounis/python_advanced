from itertools import tee, islice

iterator = (i for i in range(20))

it1, it2, it3, it4, it5, it6 = tee(iterator, 6)
print(list(it1))
print(list(it2))
print(list(it3))

print(list(islice(it4, 10)))
print(list(islice(it5, 5, 10)))
print(list(islice(it6, 5, 10, 2)))