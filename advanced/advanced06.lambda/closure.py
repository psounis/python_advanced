def f(x):
    return lambda y: x ** y


g = f(2)

print(g(10))
print(g.__closure__)
print(g.__code__.co_freevars)
for item in g.__closure__:
    print(item.cell_contents)


