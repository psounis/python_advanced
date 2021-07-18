from collections import OrderedDict

d = OrderedDict()

d[1] = 11
d[2] = 12
d[3] = 13
d[0] = 10

for k,v in d.items():
    print(f"{k}: {d[k]}")

print(d.popitem(last=False))

print("="*25)
for k,v in d.items():
    print(f"{k}: {d[k]}")
