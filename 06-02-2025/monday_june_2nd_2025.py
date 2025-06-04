from typing import *
from collections import defaultdict, deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        adj = defaultdict(list)
        deg = defaultdict(int)

        m,n = len(matrix), len(matrix[0])

        def validNeighbour(i, j, original_val):
            if i >= 0 and i < m and j >= 0 and j < n and matrix[i][j] > original_val:
                return True
            return False
    
        for i in range(m):
            for j in range(n):
                deg[(i, j)] = 0
    
        for i in range(m):
            for j in range(n):
                for delta_i, delta_j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    if validNeighbour(i + delta_i, j + delta_j, matrix[i][j]):
                        adj[(i, j)].append((i + delta_i, j + delta_j))
                        deg[(i + delta_i, j + delta_j)] += 1
        
        queue = deque()
        for cell, val in deg.items():
            if val == 0:
                queue.append((cell, 1))
            
        max_length = 0
        ans = 0

        while queue:
            cell, depth = queue.popleft()
            ans = max(depth, ans)
            for neighbour in adj[cell]:
                deg[neighbour] -= 1
                if deg[neighbour] == 0:
                    queue.append((neighbour, depth + 1))
                    deg[neighbour] -= 1
        
        return ans
    
s = Solution()
print(s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))