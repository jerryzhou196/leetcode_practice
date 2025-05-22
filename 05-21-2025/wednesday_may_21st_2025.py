from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, len(nums)
        count = 0

        while target > 0:
            if not nums:
                return 0

            while left <= right:
                m = (left + right) // 2
                if nums[m] == target:
                    return count + 1
                elif target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1

            target -= nums[right]
            nums.pop(right)

        return right

        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # [0, 1, 2, 3, 4, 5, ^, 7, 8]

        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # [0, 1, 2, 3, ^, 5, 6, 7, 8]

        # [1,2,5,6,7,9,10]
        # [1, , , , , ,  ]

        # [1, 2, 3]
        # [0, 1, 2]

        # 9 / 2 = 4.5 = 4

        # [0, 1, 2]
        # 0 + 2 = 2 / 2 = 1
