"""Auto-generated on Wednesday, July 02, 2025."""

from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target: return m
            if target < nums[m]: 
                right = m - 1
            if target > nums[m]: 
                left = m + 1
            
        return -1