# This file is used to run scripts that require the importing of modules
from data_structures import linkedList as ds
from problems.ctci import e2_8_loop as pb


i = ds.List()
i.append(1)
i.append(2)
i.append(3)
n = i.append(4)
i.append(5)
i.append(6)

i.appendNode(n)

o = pb.loop(i)
print(o.element)