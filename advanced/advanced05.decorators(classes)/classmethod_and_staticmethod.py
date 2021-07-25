class MyClass:
    objects_initiated = 0

    def __init__(self, x, y):
        MyClass.objects_initiated += 1
        self.x = x
        self.y = y

    @staticmethod
    def print_cnt_objects():
        print(MyClass.objects_initiated)

    @classmethod
    def constructJustX(cls, x):
        print(cls.__name__)
        print(cls.__dict__)
        return cls(x, 0)


ob1 = MyClass(1, 1)
ob2 = MyClass(2, 1)
MyClass.print_cnt_objects()

ob3 = MyClass.constructJustX(3)
MyClass.print_cnt_objects()