def decorate_with_lines(func):
    def dec(*args, **kwargs):
        print("=" * 20)
        func(*args, **kwargs)
        print("=" * 20)

    return dec


@decorate_with_lines
def some_func(a,b):
    print(a*b)

some_func(5,10)
