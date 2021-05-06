# CTCI E2.8: given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists):
# Example: A - B - C - D - E -C
# Output: C

from data_structures import linkedList as ll

def loop(l1: ll.List) -> ll.Node:
    s = l1.head
    f = l1.head

    while f != None and f.next != None:
        s = s.next
        f = f.next.next

        if s == f:
            break

    if f == None or f.next == None:
        return None
    
    f = l1.head

    while f != s:
        f = f.next
        s = s.next
    
    return f