# CTCI 3.3: Imagine a literal stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely starta new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as if there were just a single stack).

from typing import Collection
from data_structures import linkedList as ll

class StackOfPlates:
    def __init__(self) -> None:
        # for brevity, we will consider the Python array as a Stack data structure
        
        self.list = ll.List()
        self.maxPerStack = 4

    def push(self, e:int) -> None:
        if len(self.list) == 0 or len(self.lastStack()) >= self.maxPerStack:
            self.list.append([])

        self.lastStack().append(e)

    def lastStack(self):
        return self.list.tail.element

    def pop(self) -> int:
        if len(self.list) == 0:
            return None
        
        e = self.lastStack().pop()

        if len(self.lastStack()) == 0:
            self.list.removeNode(self.list.tail)

        return e