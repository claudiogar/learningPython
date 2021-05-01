# This file is used to run scripts that require the importing of modules
from data_structures import linkedList as ds
from problems import e2_2_kthToLast as pb



i = ds.List()
i.append(1)
i.append(2)
i.append(1)
i.append(2)
i.append(3)

i = pb.kthToLast(i, 2)
print(i)