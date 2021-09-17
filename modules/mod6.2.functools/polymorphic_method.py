from functools import singledispatchmethod


class MyClass:
    @singledispatchmethod
    def my_print(self, x):
        raise NotImplementedError("doesn't support this")


    @my_print.register
    def my_print_var(self, arg: int):
        print("int")

    @my_print.register
    def my_print_var(self, arg: float):
        print("float")


c = MyClass()
c.my_print(54)
c.my_print(2.1)
c.my_print("str")
