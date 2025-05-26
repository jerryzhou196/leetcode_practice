from typing import *

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        array = []
        dp = [0 for _ in range(len(nums))]

        def dfs(index, parity = True): 
            if index == len(nums):
                if parity: return 0
                if not parity: return -float('inf')
        
            return max(dfs(index + 1, not parity) + (nums[index] ^ k),
                     dfs(index + 1, parity) + (nums[index]))
        
        return dfs(0)

nums = [7,7,7,7,7,7]
k = 3
edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
s = Solution()

print(s.maximumValueSum(nums, k, edges))


