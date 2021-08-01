def f(x, y):
    return x(y)
print(f(lambda x: x*x, 6))