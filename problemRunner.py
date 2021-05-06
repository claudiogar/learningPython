# This file is used to run scripts that require the importing of modules
from data_structures import linkedList as ds
from problems.ctci import e2_6_palindrome as pb


i = ds.List()
i.append(1)
i.append(2)
i.append(3)
i.append(2)
i.append(4)
i.append(2)
i.append(1)
o = pb.isPalindrome(i)
print(o)

j = ds.List()
j.append(1)
j.append(2)
j.append(3)
j.append(2)
j.append(3)
j.append(2)
j.append(1)


o = pb.isPalindrome(j)
print(o)