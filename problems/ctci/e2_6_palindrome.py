# CTCI E2.6: Implement a function to check if a linked list is palindrome.

from data_structures import linkedList as ll

def isPalindrome(list:ll.List) -> bool:
    s:ll.Node = list.head
    f:ll.Node = list.head

    if s == None or s.next == None:
        return True

    stack = []
    count = 1
    while f != None:
        stack.append(s.element)
        s = s.next
        f = f.next

        if f != None:
            f = f.next
        count+=1

    if count%2 == 1:
        stack.pop()

    while s != None:
        e = s.element
        if e != stack.pop():
            return False
        s = s.next
    return True