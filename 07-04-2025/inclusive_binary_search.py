from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right] or len(nums) == 1:
            return nums[left]
        
        while left <= right:
            m = (left + right) // 2
            if m > 0 and nums[m - 1] > nums[m]:
                return nums[m]

            if nums[0] <= nums[m]:
                left = m + 1
            else:
                right = m - 1