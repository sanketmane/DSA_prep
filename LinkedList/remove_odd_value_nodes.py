# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

# Solution to remove nodes containing odd values in it
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        if A == None:
            return A
        head = A
        temp = head
        while temp != None and temp.next != None: # temp != None is important to prevent null error
            if temp.next.val % 2 != 0:
                temp.next = temp.next.next
            else:
                temp = temp.next # putting this as else part is important otherwise you will get wrong ans
        if head.val % 2 != 0:
            head = head.next
        return head
