from functools import partial


def power_func(x, y, a=1, b=0):
    return a*x**y + b


new_func = partial(power_func, 2, a=4)

print(new_func(4, b=1))
print(new_func(1))
