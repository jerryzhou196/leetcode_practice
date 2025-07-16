from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            print(f"left: {left}, right: {right}")
            if target == nums[m]: return m
            if nums[left] <= nums[m]:
                if target >= nums[left] and target <= nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if target > nums[m] and target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1

        return -1





