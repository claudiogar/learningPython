# This file is used to run scripts that require the importing of modules
from problems.ctci import e3_2_stackMin as pb

stack = pb.Stack()

stack.push(4)
stack.push(2)
stack.push(3)
stack.push(1)

print(stack.min())