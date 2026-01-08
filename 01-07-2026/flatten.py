"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None

        start = Node(None, None, head, None)
        head.prev = start

        def dfs(curr, prev):
            if not curr: 
                return prev 

            curr.prev = prev
            prev.next = curr

            temp = curr.next
            tail = dfs(curr.child, curr)
            curr.child = None
            return dfs(temp, tail)

        dfs(head, start)
        head.prev = None
        return head 
