# CTCI e3.4: Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []
        self.phase = 0
    
    def push(self, e:int):
        if self.phase == 1:
            while len(self.s2) > 0:
                o = self.s2.pop()
                self.s1.append(o)
        self.phase = 0
        self.s1.append(e)

    def pop(self) -> int:
        if self.phase == 0:
            while len(self.s1) > 0:
                e = self.s1.pop()
                self.s2.append(e)
        
        self.phase = 1
        if len(self.s2) == 0:
            return None

        return self.s2.pop()
        