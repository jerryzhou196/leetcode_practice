from typing import *

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(curr, n):
            if curr > n: return
            if curr != 0.1:
                ans.append(curr)
            curr = int(curr * 10)

            for i in range(10):
                dfs(curr + i, n)
        
        dfs(0.1, n)
        return ans
    


