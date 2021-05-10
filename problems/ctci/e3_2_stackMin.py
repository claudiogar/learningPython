# CTCI 3.2: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time.

class StackNode:
    def __init__(self) -> None:
        self.element:int = None
        self.min:int = None

class Stack:
    def __init__(self) -> None:
        self.array = []

    def push(self, e: int) -> None:
        n = StackNode()
        n.element = e

        if self.isEmpty() or self.min() >= e:
            n.min = e
        elif self.min() < e:
            n.min = self.array[len(self.array)-1].min

        self.array.append(n)

    def count(self) -> int:
        return len(self.array)

    def isEmpty(self):
        return len(self.array) == 0

    def peek(self) -> int:
        if self.isEmpty():
            return None
        else:
            return self.array[len(self.array)-1].element
    
    def pop(self) -> int:
        if self.isEmpty():
            return None
        else:
            return self.array.pop().element

    def min(self) -> int:
        if self.isEmpty():
            return None
        
        return self.array[len(self.array)-1].min
        

        
