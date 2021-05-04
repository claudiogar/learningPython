# CTCI E2.3: Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node, not necessarily the exact middle) if a singly linked list, given only access to that node.

from data_structures import linkedList as ll

def removeMiddle(n: ll.Node) -> None:
    while n != None and n.next != None:
        n.element = n.next.element
        n.next = n.next.next
        n = n.next