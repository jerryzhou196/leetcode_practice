from typing import List
from heapq import heappush, heappop

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)


nums = [2,0,2,3,3,2,1]
queries = [[0,2],[0,2],[1,1],[2,2], [1,2], [3,6], [3,6], [3,6]]
s = Solution()
print(s.maxRemoval(nums, queries))