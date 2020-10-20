def f():
    yield 1
    yield 2
    yield 3

it = f()
for _ in range(3):
    print(next(it))
