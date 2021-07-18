from collections import Counter

l = [1, 2, 3, 2]
cl = Counter(l)
print(cl)

phrase = "Winter is coming"
cphrase = Counter(phrase)
print(cphrase, cphrase["i"])

t = [[1, 2], [1]]
ct = Counter(t) # error: elems=>unhashable
