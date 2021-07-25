import time


def decorate_with_lines(func):
    def dec(arg):
        print("-"*20)
        res = func(arg)
        print("-"*20)
        return res
    return dec

def timeit(func):
    def decorator(*args, **kwargs):
        t0 = time.time()
        ret = func(*args, **kwargs)
        t1 = time.time()
        print("Total time: " + str(t1-t0))
        return ret

    return decorator

def memoize(func):
    def decorator(arg):

        if arg in results_memory:
            return results_memory[arg]
        else:
            results_memory[arg] = func(arg)
            return results_memory[arg]

    results_memory = {}
    return decorator

def valid_int_gt_zero(func):
    def decorated(val):
        if not isinstance(val, int):
            raise TypeError("Not an integer")
        elif val < 0:
            raise ValueError("Negative value")
        else:
            return func(val)

    return decorated


@timeit
@decorate_with_lines
@valid_int_gt_zero
def fib(n):
    @memoize
    def recursive(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return recursive(n - 1) + recursive(n - 2)

    print(f"fib({n})={recursive(n)}")

fib(68)
