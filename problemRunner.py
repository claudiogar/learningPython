# This file is used to run scripts that require the importing of modules
from problems.ctci import e3_4_queueWithStacks as pb

s = pb.MyQueue()

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
print(len(s.s1))
print(len(s.s2))
