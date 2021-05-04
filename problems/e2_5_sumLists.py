# CTCI 2.5: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. (You are not allowed to "cheat" and just convert the linked list to an integer).

# Example:
# Input: 7 - 1 - 6 + 5 - 9 - 2. That is, 617 + 295.
# Output: 2 - 1 - 9, that is 912

from data_structures import linkedList as ll

def add(l1: ll.List, l2:ll.List) -> ll.List:
    output:ll.List = ll.List()
    ptr1 = l1.head
    ptr2 = l2.head
    rem = 0

    while ptr1 != None and ptr2 != None:
        v1 = 0
        v2 = 0
        if ptr1 != None:
            v1 = ptr1.element
            ptr1 = ptr1.next
        if ptr2 != None:
            v2 = ptr2.element
            ptr2 = ptr2.next
        
        sum = rem + v1 + v2
        if sum > 9:
            rem = 1
            sum = sum - 10
        else:
            rem = 0

        output.append(sum)

    return output