# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_list = []
        ans = curr = ListNode(-1, None)
        for new_node in lists:
            for node in lists:
                new_list.append(node)
                lists[node] = lists[node].next

            new_list = sorted(new_list)
            for node in new_list:
                curr.next = ListNode(node)
                curr = curr.next
        
        return ans