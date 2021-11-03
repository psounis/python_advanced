from operator import methodcaller

class A:
    def __init__(self):
        self.x = 1
        self.y = 2

    def __getitem__(self, item):
        if item == 0:
            return self.x
        else:
            return self.y

    def f(self, arg):
        return self.x + arg


class B:
    def __init__(self):
        self.x = 11
        self.y = 21

    def __getitem__(self, item):
        if item == 0:
            return self.x
        else:
            return self.y

    def f(self, arg):
        return self.x + arg


a = A()
b = B()

method_f = methodcaller("f", 100)
print(method_f(a))
print(method_f(b))
