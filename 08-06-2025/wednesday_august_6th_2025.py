
from typing import *

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # [1, -3, 4, -2, -2]


        for num in nums:
            if nums[abs(num)] < 0:
                return num
            else:
                nums[abs(num)] = -nums[num]

        