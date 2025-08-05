"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import *
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def printSeen(self, seen):
        for node in seen.keys():
            print(f"key ({node.val if node else None}): {seen[node].val if seen[node] else None}")
            

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}
        node = head
        while node and node.next:
            # for first node
            if node not in seen:
                seen[node] = Node(node.val) 

            if node.next and not node.next in seen:
                seen[node.next] = Node(node.next.val)

            if node.random and not node.random in seen:
                seen[node.random] = Node(node.random.val)

            seen[node].next = seen[node.next]
            seen[node].random = seen[node.random] if node.random in seen else None

            node = node.next

        return seen[head]
    
s = Solution()
n1 = Node(7)      
n2 = Node(13)
n3 = Node(11)
n4 = Node(10)
n5 = Node(1)

# next pointers
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None     # tail

# random pointers
n1.random = None   # 7 → ∅
n2.random = n1     # 13 → 7
n3.random = n5     # 11 → 1
n4.random = n3     # 10 → 11
n5.random = n1     # 1  → 7

head = n1          # entry-point for the list
# ----------------------------------------------------------------------

# Example invocation
s = Solution()
cloned_head = s.copyRandomList(head)      # deep-copies the test list
