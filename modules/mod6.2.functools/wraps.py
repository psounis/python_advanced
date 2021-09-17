from functools import wraps


def decorate_with_lines(func):
    @wraps(func)
    def dec():
        """ inner docstring """
        print("=" * 20)
        func()
        print("=" * 20)

    return dec


@decorate_with_lines
def some_func():
    """ some_func docstring """
    print("I did many things.. ")



print(some_func.__name__)
print(some_func.__doc__)
