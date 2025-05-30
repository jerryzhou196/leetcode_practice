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
            odd_sum = dfs(1, -1, True, adj)

            useEven = True 

            for node in range(n):
                ans[node] = even_sum if useEven else odd_sum
                even_sum = not even_sum

            return ans
        
        adj1, adj2 = DefaultDict(list), DefaultDict(list)

        ans = build(edges1, adj1)
        largest = max(build(edges2, adj2))
        return [num + largest for num in ans]