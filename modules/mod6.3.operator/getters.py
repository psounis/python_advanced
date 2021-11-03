from operator import itemgetter, attrgetter

class A:
    def __init__(self):
        self.x = 1
        self.y = 2

    def __getitem__(self, item):
        if item == 0:
            return self.x
        else:
            return self.y


class B:
    def __init__(self):
        self.x = 11
        self.y = 21

    def __getitem__(self, item):
        if item == 0:
            return self.x
        else:
            return self.y


a = A()
b = B()

attr_x = attrgetter("x")
print(attr_x(a))
print(attr_x(b))

item = itemgetter(1)
print(item(a))
print(item(b))
