from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def revList(self, node, prev=None):
        if node:
            temp = node.next
            node.next = prev
            return node if not temp else self.revList(temp, node)

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # print(f"mid-point: {slow.val}")
        
        end = self.revList(slow, )
        start = head 

        while start: 
            # print(f"start: {start.val}")
            # print(f"end: {end.val}")
            temp = start.next
            start.next = end
            temp1 = end.next 
            end.next = temp
            start = temp
            end = temp1