# This file is used to run scripts that require the importing of modules
from data_structures import linkedList as ds
from problems.ctci import e2_7_intersect as pb


i = ds.List()
i.append(1)
i.append(2)
i.append(3)
n = i.append(4)
i.append(5)
i.append(6)

j = ds.List()
j.append(1)
j.appendNode(n)

o = pb.intersect(i, j)
print(o.element)