from operator import itemgetter

A = [(1,19,29), (5, 14, 24), (9, 11, 27)]

for i in range(3):
    print(sorted(A, key=itemgetter(i)))