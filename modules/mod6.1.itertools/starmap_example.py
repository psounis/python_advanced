from itertools import starmap, product

def func(a,b,c,d):
    return abs(a-b)+abs(b-c)+abs(c-d)
print(list(product([1,2,3],[1,2,4],[3,5,2],[4,1,2])))
iterator = starmap(func, product([1,2,3],[1,2,4],[3,5,2],[4,1,2]))
print(min(iterator))