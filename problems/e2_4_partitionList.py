# CTCI E2.4: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greather than or equal to x.  (IMPORTANT: The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.)

from data_structures import linkedList as ll
def partition(list:ll.List, x:int) -> ll.List:
    left = ll.List()

    ptr = list.head

    while ptr != None:
        ele = ptr
        if ele is None:
            break

        ptr = ele.next

        if ele.element < x:
            left.append(ele.element)
            list.removeNode(ele)
        
    
    left.tail.next = list.head
    left.tail = list.tail
    return left
    