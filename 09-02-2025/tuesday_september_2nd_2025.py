# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists_dict = {}
        for index, l in enumerate(lists):
            if l:
                lists_dict[index] = l 
        
        # print(lists_dict)
        
        ans = curr = ListNode() 
        while lists_dict:
            curr_smallest = next(iter(lists_dict)) 
            for index in lists_dict.keys():
                if lists_dict[curr_smallest].val > lists_dict[index].val:
                    curr_smallest = index

            # print(lists_dict[curr_smallest].val)

            ans.next = lists_dict[curr_smallest]
            ans = ans.next

            if lists_dict[curr_smallest].next:
                lists_dict[curr_smallest] = lists_dict[curr_smallest].next 
            else:
                del lists_dict[curr_smallest]
        
        return curr.next
        