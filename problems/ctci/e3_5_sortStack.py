# CTCI 3.5: Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure. The stack supports the following operations: push, pop, peek, and isEmpty.

class SortedStack:
    def __init__(self):
        self.stack = []
        self.side = []
        pass

    def push(self, e):
        if self.isEmpty():
            self.stack.append(e)
            pass

        p = self.peek()
        while p < e:
            v = self.pop()
            self.side.push(v)
            p = self.peek()
        
        self.stack.append(e)
        while len(self.side) > 0:
            v = self.side.pop()
            self.stack.push(v)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.pop()
        return None
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0