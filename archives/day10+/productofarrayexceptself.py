# nums: [1, 2, 3, 4]
# L: [1, 1, 2, 6]
# R: [1, 4, 12, 24]
from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        l = [0 for _ in range(len(nums))]
        r = [0 for _ in range(len(nums))]
        l[0] = 1
        r[0] = 1
        for i in range(1, len(nums)):
            l[i] = l[i - 1] * nums[i - 1]
            r[i] = r[i - 1] * nums[len(nums) - i]
        for i in range(len(nums)):
            ans[i] = l[i] * r[len(nums) - i - 1]
        return ans


inp = [1, 2, 3, 4]
sln = Solution()
sln.productExceptSelf(inp)
