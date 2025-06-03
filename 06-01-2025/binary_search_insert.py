from typing import *


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] >= target:
                right = m - 1
            else:
                left = m + 1

        return left


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 1))
