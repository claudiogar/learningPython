class TwoWaysNode:
    def __init__(self, e):
        self.next = None
        self.prev = None
        self.value = e
    
class DoubleLinkedList:
    head = None
    tail = None
    
    def count(self):
        h = self.head
        i = 0

        while h:
            h = h.next
            i = i + 1
        
        return i
    
    def add(self, e):
        node = TwoWaysNode(e)
        if self.count() == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def remove(self, e):
        h = self.head

        while h and h.value != e:
            h = h.next
        
        if not h:
            pass

        h.prev.next = h.next
        h.next.prev = h.prev

    def print(self):
        h = self.head
        while h:
            print(h.value)
            h = h.next
