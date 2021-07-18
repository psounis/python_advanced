from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "a": 6}

cm = ChainMap(dict1, dict2, dict3)
print(cm)

print(cm["b"])
print(cm["a"])

pylookup = ChainMap(locals(), globals())
print(pylookup)
