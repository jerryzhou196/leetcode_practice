from typing import *
from copy import deepcopy
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        nums_copy = deepcopy(nums) 
        for i, num in enumerate(nums): 
            for query in queries: 
                if i <= query[1] and i >= query[0]: 
                    nums_copy[i] = max(nums_copy[i] - 1, 0)

        return not any([nums_copy[i] != 0 for i in range(len(nums))]) 

s = Solution()
print(s.isZeroArray([4,3,2,1], [[0,2]]))

# Input: nums = [1,0,1], queries = [[0,2]]
# ans: [0,0,0]

# Input: nums = [4,3,2,1], queries = [[1,3],[0,2]...]
# ans: [0,0,0]

# Input: nums = [9, 2, 3, 4, 4, 5], queries = []
# ans: []

# max_subtract: [0, 0, 0]
# ans: []


