def f():
    i=1
    while True:
        yield i
        i+=2


it = f()
for i in it:
    print(i)
    if i==101:
        it.close()
