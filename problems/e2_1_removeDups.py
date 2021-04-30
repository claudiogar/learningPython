# CTCI E2.1: Write code to remove duplicates from an unsorted linked list.
from data_structures import linkedList as ds

def removeDuplicates(list:ds.List) -> ds.List:
    alreadySeen = set()
    node = list.head
    prev = None

    while node != None:
        if node.element in alreadySeen:
            prev.next = node.next
        else:
            alreadySeen.add(node.element)
            prev = node
        node = node.next
    return list

