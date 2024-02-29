from pickle import load

class Data:
    def __init__(self, alist, adict, anint, aset, adata):
        self.alist = alist
        self.adict = adict
        self.anint = anint
        self.aset = aset
        self.adata = adata

    def __str__(self):
        return str(self.alist)+","+str(self.adict)+","