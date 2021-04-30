# This file is used to run scripts that require the importing of modules
from data_structures import linkedList as ds
from problems import e2_1_removeDups as pb



i = ds.List()
i.append(1)
i.append(2)
i.append(1)
i.append(2)
i.append(3)

i = pb.removeDuplicates(i)
h = i.head
while(h != None):
    print(h.element)
    h = h.next
