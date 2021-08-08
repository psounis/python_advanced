from itertools import chain, zip_longest

a = (i for i in range(10))
b = (i for i in range(10,15))
c = (i for i in range(20,25))
for i in chain(a,b,c):
    print(i, end=" ")

print()
print(list(zip([1,2,3],[3,4],[5])))
print(list(zip_longest([1,2,3],[3,4],[5], fillvalue=0)))
