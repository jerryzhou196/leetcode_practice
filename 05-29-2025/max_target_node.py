from typing import *

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(node, prev, k, adj):
            ans = 1
            if k < 0: 
                return 0
            for neighbour in adj[node]:
                if neighbour != prev:
                    ans += dfs(neighbour, node, k - 1, adj)
            return ans
        
        def build(edges, k, adj):
            n = len(edges) + 1
            ans = [0] * n
            for x, y in edges:
                adj[x].append(y)
                adj[y].append(x)

            for i in range(n):
                ans[i] = dfs(i, -1, k, adj)

            return ans
        
        adj1, adj2 = DefaultDict(list), DefaultDict(list)

        ans = build(edges1, k, adj1)
        largest = max(build(edges2, k - 1, adj2))
        return [num + largest for num in ans]


s = Solution()
print(s.maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 2))