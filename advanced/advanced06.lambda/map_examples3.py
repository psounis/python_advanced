print(list(map(lambda x: x*x*x, [1,2,3])))
print([x*x*x for x in [1,2,3]])

A=[1,2,3]
B=[4,5,6]
print(list(map(lambda x,y: x+y, [1,2,3], [4,5,6])))
print([A[i]+B[i] for i in range(len(A))])