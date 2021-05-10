# This file is used to run scripts that require the importing of modules
from problems.ctci import e3_3_stackOfPlates as pb

s = pb.StackOfPlates()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.list.count())

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.list.count())