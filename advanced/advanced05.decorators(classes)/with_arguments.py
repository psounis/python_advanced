
# decorator without arguments
def line_below(func):
    def line(m, *args):
        func(*args)
        for i in range(m):
            for arg in args:
                print(arg, end="")

    return line


@line_below
def my_print(m, *args):
    print("test")


my_print(5, "*", "-", "*")
print()


# decorator with arguments:


def lines_below(n):
    def line_below(func):
        def line(m, *args):
            func(*args)
            for _ in range(n):
                for i in range(m):
                    for arg in args:
                        print(arg, end="")
                print()

        return line

    return line_below

@lines_below(n=4)
def my_print2(m, *args):
    print("test")

my_print2(5, "*", "-", "*")
