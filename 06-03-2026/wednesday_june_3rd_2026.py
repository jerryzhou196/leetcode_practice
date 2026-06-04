"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}
        def dfs(node):
            if not node:
                return None
            # print(node.val, node.val in created)
            if node.val in created: 
                return created[node.val]

            created[node.val] = Node(node.val)
            for neighbour in node.neighbors:
                created[node.val].neighbors.append(dfs(neighbour))

            return created[node.val] 
            
        return dfs(node)

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        queue = deque()
        n, m = len(rooms), len(rooms[0])
        for i in range(n):
            for j in range(m): 
                if rooms[i][j] == 0:
                    queue.append((0,i, j))
        
        # print(queue)
        
        while queue: 
            depth, y, x = queue.popleft()
            # print(depth, y, x)

            if depth != 0 and rooms[y][x] != 2147483647:
                continue

            rooms[y][x] = depth 

            for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                if y + i < 0 or y + i >= n or x + j < 0 or x + j >= m or rooms[y + i][x + j] != 2147483647: 
                    continue 
                queue.append((depth + 1, y + i, x + j))

        return rooms
            
                
                    
        
       
            
        
