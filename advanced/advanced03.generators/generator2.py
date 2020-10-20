def f():
    for i in range(10):
        yield i


it = f()
for i in it:
    print(i)

it = f()
while True:
    try:
        print(next(it))
    except StopIteration:
        break