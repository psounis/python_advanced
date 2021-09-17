from functools import singledispatch


@singledispatch
def my_print(x):
    raise NotImplementedError("doesn't support this")


@my_print.register
def my_print_var(arg: int):
    print("int")

@my_print.register
def my_print_var(arg: float):
    print("float")


my_print(54)
my_print(2.1)
my_print("str")
