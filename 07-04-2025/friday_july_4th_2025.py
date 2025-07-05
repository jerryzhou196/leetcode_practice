from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            m = (left + right) // 2
            if nums[left] < nums[m]:
                left = m
            else:
                right = m
        
        return nums[left + 1] if len(nums) > 1 else nums[0]