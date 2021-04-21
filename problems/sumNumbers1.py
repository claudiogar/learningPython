# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = []

        currentA = l1
        currentB = l2
        carry = 0
        while currentA is not None or currentB is not None:
            d1 = 0
            d2 = 0
            if currentA is not None:
                d1 = currentA.val
                currentA = currentA.next

            if currentB is not None:
                d2 = currentB.val
                currentB = currentB.next

            sum = d1+d2+carry
            if sum > 9:
                carry = 1
                sum = sum-10
            else:
                carry = 0
            output.append(sum)
        
        if carry == 1:
            output.append(1)
        
        print(output)
        return self.toList(output)

    def toList(a) -> ListNode:
        if len(a) == 0:
            return ListNode
        
        head = ListNode
        tail = head

        i = 0
        while i < len(a):
            tail.val = a[i]
            i+=1

            if( i < len(a)):
                tail.next = ListNode
                tail = tail.next
        
        return head


l1 = ListNode(9, ListNode(9, ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9,ListNode(9))))

output = Solution.addTwoNumbers(Solution,l1,l2)
