"""Auto-generated on Tuesday, July 15, 2025."""

from collections import deque 
from typing import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        inc = deque([[nums[0], 0]])
        ans = []

        for i in range(1, k):
            if inc[-1][0] <= nums[i]:
                inc.pop()
                inc.append([nums[i], i])

        ans.append(inc[-1][0])

        for r in range(k, len(nums)):
            if inc and r - k == inc[0][1]:
                inc.popleft()
            while inc and inc[-1][0] <= nums[r]:
                inc.pop()
            inc.append([nums[r], r])

            ans.append(inc[0][0])

        return ans

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) 


