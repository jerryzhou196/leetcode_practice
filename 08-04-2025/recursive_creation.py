class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}

        def duplicate(node):
            if not node: return None
            if node in seen: return seen[node]
            seen[node] = Node(node.val)
            seen[node].next = duplicate(node.next)
            seen[node].random = duplicate(node.random)
            return seen[node]

        return duplicate(head)