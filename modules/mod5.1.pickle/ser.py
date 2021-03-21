from pickle import dump, dumps


class Data:
    def __init__(self, alist, adict, anint, aset, adata):
        self.alist = alist
        self.adict = adict
        self.anint = anint
        self.aset = aset
        self.adata = adata


l = [1, 2, 3]
print(dumps(l))

with open("data.pkl", "wb") as f:
    d1 = Data([1, 2], {1: 1, 2: 2}, 1, {1, 2}, None)
    dump(d1, f)
    d2 = Data([3], {3: 3}, 3, {3}, d1)
    dump(d2, f)
    d3 = Data([], {}, 0, set(), d2)
    dump(d3, f)
