def decorate_with_lines(func):
    def dec():
        print("=" * 20)
        func()
        print("=" * 20)

    return dec

def some_func():
    print("I did many things.. ")


decorated_func = decorate_with_lines(some_func)

decorated_func()
