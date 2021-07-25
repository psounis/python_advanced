import time


def timeit(func):
    def decorator(*args, **kwargs):
        t0 = time.time()
        ret = func(*args, **kwargs)
        t1 = time.time()
        print("Total time: " + str(t1-t0))
        return ret

    return decorator


@timeit
def dummy(n):
    for i in range(n):
        pass

dummy(100000000)
