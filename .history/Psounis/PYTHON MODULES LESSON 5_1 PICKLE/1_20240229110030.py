from pickle import dump, dumps

class Data:
    def _init__(self, alist, adict, anint, aset, adata):
        self.alist = alist
        self.adict - adict
        self.anint = anint
        self.aset = aset
        self.adata = adata

l=[1,2,3]

print(dumps(l))

with open("data.pkl", "wb") as f:
    d1=Data([1,2], {1:1, 2:2})