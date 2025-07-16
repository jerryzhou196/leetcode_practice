from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if target == nums[m]: return m
            if nums[left] > nums[right]:
                if ((nums[m] <= target and target <= nums[right]) or
                    (nums[left] <= nums[m] and nums[m] <= target) or 
                    (target <= nums[right] and nums[right] <= nums[m])):
                    left = m + 1
                else:
                    right = m - 1
            else:
                if (target > nums[m]):
                    left = m + 1
                else:
                    right = m - 1
        
        return -1
                






