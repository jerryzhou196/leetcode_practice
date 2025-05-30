from typing import *
from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        deg = [0 for _ in range(len(colors))]

        adjacency_matrix = defaultdict(list)
        queue = deque()

        f = [[0] * 26 for _ in range(len(colors))]

        for x, y in edges: 
            adjacency_matrix[x].append(y)
            deg[y] += 1
        
        queue += [i for i, val in enumerate(deg) if deg[i] == 0]
        ans = 0
        visited_nodes = 0 
        
        while queue:
            node = queue.popleft()
            visited_nodes += 1

            f[node][ord(colors[node]) - ord('a')] += 1
            ans = max(ans, f[node][ord(colors[node]) - ord('a')])

            for neighbour in adjacency_matrix[node]: 
                deg[neighbour] -= 1
                for i in range(26): 
                    f[neighbour][i] = max(f[node][i], f[neighbour][i])

                if deg[neighbour] == 0:
                    queue.append(neighbour)
            
        return ans if visited_nodes < len(colors) else -1

s = Solution()
print(s.largestPathValue("abc", [[0,1], [1,2], [2,1]]))
