from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = end = head
        count = n + 1
        while count and end:
            end = end.next
            count -= 1
        
        while end:
            end = end.next
            start = start.next
        
        start.next = start.next.next
        return head


        
        

        
            

        



        