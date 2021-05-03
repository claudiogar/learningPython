# This file is used to run scripts that require the importing of modules
from data_structures import linkedList as ds
from problems import e2_3_deleteMiddleNode as pb



i = ds.List()
i.append(1)
i.append(2)
node = i.append(3)
i.append(4)

pb.removeMiddle(node)
i.print()