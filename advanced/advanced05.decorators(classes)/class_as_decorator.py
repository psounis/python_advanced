class decorate_with_lines:
    def __init__(self, decorated):
        self.decorated = decorated

    def __call__(self):
        print("-"*20)
        ob = self.decorated()
        print("-"*20)
        return ob


@decorate_with_lines
class MyClass:
    def __init__(self):
        print("initializing...")

    def func(self):
        print("in func")



c = MyClass()
c.func()
