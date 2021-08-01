def square(x):
    return x*x

print(list(map(square, [1,2,3])))

# with lambda:

print(list(map(lambda x: x*x*x, [1,2,3])))