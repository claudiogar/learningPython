# This file is used to run scripts that require the importing of modules
from data_structures import linkedList as ds
from problems.ctci import e2_5_sumLists as pb


i = ds.List()
i.append(7)
i.append(1)
i.append(6)

j = ds.List()
j.append(5)
j.append(9)
j.append(2)

i = pb.add(i, j)

h = i.head

while h != None:
    print(h.element)
    h = h.next