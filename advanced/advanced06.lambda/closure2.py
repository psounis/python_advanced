l = []
for i in range(3):
    l.append(lambda: i)

for it in l:
    print(it())


# solution:

l = []
for i in range(3):
    l.append(lambda n=i: n)

for it in l:
    print(it())
