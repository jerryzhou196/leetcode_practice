from typing import *

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(node, prev, isEven, adj):
            ans = 1 if isEven else 0
            for neighbour in adj[node]:
                if neighbour != prev:
                    ans += dfs(neighbour, node, not isEven, adj)
            return ans
        
        def build(edges, adj):
            n = len(edges) + 1
            ans = [0] * n
            for x, y in edges:
                adj[x].append(y)
                adj[y].append(x)

            even_sum = dfs(0, -1, True, adj)
            odd_sum = dfs(adj[0][0], -1, True, adj)

            def markSum(node, prev, isEven, adj):
                ans[node] = odd_sum if not isEven else even_sum
                for neighbour in adj[node]:
                    if neighbour != prev: 
                        markSum(neighbour, node, not isEven, adj)
            markSum(0, -1, True, adj)
            
            return ans
        
        adj1, adj2 = DefaultDict(list), DefaultDict(list)

        ans = build(edges1, adj1)
        largest = max(build(edges2, adj2))
        return [num + largest for num in ans]

# Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
  
s = Solution()
print(s.maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]))