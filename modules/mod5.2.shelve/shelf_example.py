from shelve import open

class Data:
    def __init__(self, alist, adict, anint, aset, adata):
        self.alist = alist
        self.adict = adict
        self.anint = anint
        self.aset = aset
        self.adata = adata

shelf = open("data.shelf", writeback=True)

shelf["int"] = 1
shelf["dict"] = {"a": 1, "b": 2}
shelf["set"] = {1, 2, 3}
shelf["object"] = Data([1, 2], {1: 1, 2: 2}, 1, {1, 2}, None)

shelf.close()

with open("data.shelf", writeback=True) as shelf:
    shelf["int"] = 2
    for k, v in shelf.items():
        print(k, v)