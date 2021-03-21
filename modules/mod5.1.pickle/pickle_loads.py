from pickle import load


class Data:
    def __init__(self, alist, adict, anint, aset, adata):
        self.alist = alist
        self.adict = adict
        self.anint = anint
        self.aset = aset
        self.adata = adata

    def __str__(self):
        return str(self.alist) + ", " + str(self.adict) + ", " + \
               str(self.anint) + ", " + str(self.aset) + \
               ", Data(" + str(self.adata) + ")"


with open("data.pkl", "rb") as f:
    try:
        ob = load(f)
        while ob is not None:
            print(ob)
            ob = load(f)
    except EOFError:
        pass
