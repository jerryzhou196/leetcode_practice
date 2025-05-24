from typing import *


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        deltaArray = [0] * (len(nums) + 1)
        for left, right in queries:
            deltaArray[left] += 1
            deltaArray[right + 1] -= 1
        operationCounts = []
        currentOperations = 0
        for delta in deltaArray:
            currentOperations += delta
            operationCounts.append(currentOperations)
        for operations, target in zip(operationCounts, nums):
            if operations < target:
                return False
        return True


s = Solution()
s.isZeroArray([4, 3, 2, 1], queries=[[1, 3], [0, 2]])

from typing import *

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        delta = [0 for _ in range(len(nums) + 1)]
        for start, end in queries: 
            delta[start] += 1
            delta[end + 1] -= 1

        toggle = 0
        for i, num in enumerate(nums): 
            toggle += delta[i]
            if num > toggle: 
                return False
        return True 

delta = [1, 0, 1, 0, 0, 0, 0]
arr = [1,2,4,2,5,4]
queries = [[0,1], [2,5], [3,4]]

s = Solution()
s.isZeroArray([1,2,4,2,5,4], [[0,1], [2,5], [3,4]])

# Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]