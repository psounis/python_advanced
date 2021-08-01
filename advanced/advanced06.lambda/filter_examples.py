def is_odd(x):
    return x%2 == 1

print(list(filter(is_odd, [1,2,3,4,5])))
print(filter(is_odd, [1,2,3,4,5]))

# with lambda:

print(list(filter(lambda x: x%2==0, [1,2,3,4,5])))