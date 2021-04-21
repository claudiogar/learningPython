class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, e):
        node = Node(e)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def count(self):
        i = 0
        n = Node(0)
        n.next = self.head
        while n.next is not None:
            i = i+1
            n = n.next
        return i

    def remove(self, e):
        n = Node(0)
        n.next = self.head
        while n.next and n.next.element != e:
            n = n.next
        
        if n.next:
            n.next = n.next.next

    def print(self):
        h = self.head

        while h:
            print(h.element)
            h = h.next
