# CTCI E2.7: given two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

from data_structures import linkedList as ll

def intersect(l1:ll.List, l2:ll.List) -> ll.Node:
    c1 = l1.count()
    c2 = l2.count()

    i  = 0
    h1 = l1.head
    h2 = l2.head

    if c1 > c2:
        while c1 > c2 + i:
            i += 1
            h1 = h1.next
    elif c2 > c1:
        while c1 + i < c2:
            i += 1
            h2 = h2.next
    
    while h1 != None and h2 != None:
        if h1 == h2:
            return h1
        h1 = h1.next
        h2 = h2.next
    
    return None
