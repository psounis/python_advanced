from collections import defaultdict


def func():
    return "no value"

d1 = defaultdict(func)

print(d1["a"])
print(d1)


print("="*25)

d2 = defaultdict(list)

d2["a"].append(1)
d2["b"].append(2)
print(d2)


print("="*25)

d3 = defaultdict(str)

d3["a"] += "bb"
d3["a"] += "aa"
d3["c"] += "2"
print(d3)


print("="*25) # from the docs

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d4 = defaultdict(list)
for k, v in s:
    d4[k].append(v)
print(d4)
