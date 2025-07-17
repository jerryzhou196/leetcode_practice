from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5
        ans = None
        def rev(curr, prev):
            if not curr: 
                nonlocal ans
                ans = prev
            else:
                rev(curr.next, curr)
                # print(f"setting {curr.val}.next =  {prev.val}")
                curr.next = prev

        if not head: return None
        rev(head, None) 
        return ans
        