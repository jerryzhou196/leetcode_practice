from typing import List
from heapq import heappush, heappop

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries = queries.sort(key: lambda x[0])
        operations = 0
        future_delta = [0] * (len(nums) + 1)
        heap = []
        for i, num in enumerate(nums):
            operations += future_delta[i]
            while heap and -heap[0] == i: 
                future_delta[heap[1] + 1] -= 1
                operations += 1

nums = [2,0,2,5,6,9,]
queries = [[0,2],[0,2],[1,1],]
s = Solution()
s.maxRemoval(nums, queries)