from typing import *

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            else:
                nums[abs(num)] = -nums[abs(num)]