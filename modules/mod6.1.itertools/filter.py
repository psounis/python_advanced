from itertools import dropwhile, takewhile, compress, filterfalse

elements = [1,2,3,4,5,1,2]
pred = lambda x: x<3
iterator = dropwhile(pred, elements)
for item in iterator:
    print(item)

print("="*20)
print(list(takewhile(pred, elements)))

print("="*20)
print(list(compress(elements, [1,1,1,1,0,0,1])))

print("="*20)
print(list(filterfalse(lambda x:x%2==0, elements)))