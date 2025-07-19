"""Auto-generated on Thursday, July 17, 2025."""

from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode(-1, None)
        while list1 and list2: 
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2 
                list2 = list2.next

        while list1:
            curr.next = list1
            list1 = list1.next

        while list2:
            curr.next = list2
            list2 = list2.next

        return head

