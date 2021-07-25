
def decorate_with_lines(cls):
    def dec():
        print("-"*20)
        ob = cls()
        print("-"*20)
        return ob
    return dec


@decorate_with_lines
class MyClass:
    def __init__(self):
        print("initializing...")

    def func(self):
        print("in func")


c = MyClass()
c.func()
