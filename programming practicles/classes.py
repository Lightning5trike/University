
from tkinter import *


class manager:
    def __init__(self):
        self.items = []
    
    def additem(self, item):
        self.items.append(item)
    
    def getitem(self, index):
        return self.items[index]



class item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getkey(self):
        return self.key
    
    def getvalue(self):
        return self.value

    def setkey(self, key):
        self.key = key
    
    def setvalue(self, value):
        self.value = value


def testobject():

    mgr = manager()

    item1 = item(0, 48620)
    item2 = item(1, 46970)
    item3 = item(2, 58497)

    mgr.additem(item1)
    mgr.additem(item2)
    mgr.additem(item3)

    for i in range(len(mgr.items)):
        print(mgr.getitem(i).getkey())
        print(mgr.getitem(i).getvalue())

    


