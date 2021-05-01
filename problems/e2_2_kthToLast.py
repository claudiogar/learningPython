# CTCI E2.2: Implement an algorithm to find the kth to last element of a singly linked list.

from data_structures import linkedList as ll
def kthToLast(list: ll.List, k:int) -> int:
    t = list.head
    r = list.head

    # shift the "rabbit" by k elements
    for i in range(0, k-1):
        r = r.next

        # if there are less than k nodes, there's nothing to return
        if r == None:
            return -1
    
    while r.next != None:
        t = t.next
        r = r.next
    
    return t.element
