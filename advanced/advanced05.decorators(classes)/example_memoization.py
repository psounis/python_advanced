def memoize(func):
    def decorator(arg):

        if arg in results_memory:
            return results_memory[arg]
        else:
            results_memory[arg] = func(arg)
            return results_memory[arg]

    results_memory = {}
    return decorator



@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)



print(fib(10))
