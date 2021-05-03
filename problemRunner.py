# This file is used to run scripts that require the importing of modules
from data_structures import linkedList as ds
from problems import e2_4_partitionList as pb


i = ds.List()
i.append(3)
i.append(1)
i.append(2)
i.append(4)

i = pb.partition(i, 3)
i.print()