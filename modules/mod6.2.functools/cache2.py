from functools import cache


@cache
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(fib(100))
print(fib.cache_info()) # cache stats
fib.cache_clear() # clears cache