def decorate_arg_int_not_zero(func):
    def dec(*args):
        for arg in args:
            if not isinstance(arg,int):
                print("Error: Must be integer!")
                return None
            if arg==0:
                print("Error: Must not be zero!")
                return None

        func(*args)

    return dec


@decorate_arg_int_not_zero
def some_func(a,b):
    print(a*b)

@decorate_arg_int_not_zero
def some_func1(a,b,c):
    print(a*b*c)

some_func(0,10)
some_func1(-8,10,20)
