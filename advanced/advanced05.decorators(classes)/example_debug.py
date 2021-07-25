def debug_args(func):
    def decorator(*args):
        for arg in args:
            print(repr(arg), end=", ")
        return func(*args)

    return decorator

class MyClass:
    def __init__(self):
        self.x = 5
    def __repr__(self):
        return f"MyClass({self.x})"

@debug_args
def dummy(n, ob):
    pass

dummy(5, MyClass())
