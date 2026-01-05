from collections import deque
from typing import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        ans.append(nums[dq[0]])
        
        for i in range(k, len(nums)):
            # print(f'dq: {dq}')
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i - k == dq[0]:
                dq.popleft()
            ans.append(nums[dq[0]])

        return ans 

# [1,3,-1,-3,5,3,6,7]
