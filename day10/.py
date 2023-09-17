from collections import defaultdict
from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = defaultdict(int)
        arr = [[] for _ in range(len(nums) + 1)]
        ans = []
        for element in nums:
            occurences[element] += 1

        for key, value in occurences.items():
            arr[value].append(key)

        for x in range(len(arr) - 1, -1, -1):
            if k == 0:
                return ans
            elif len(arr[x]) > 0:
                ans.extend(arr[x])
                k -= len(arr[x])


ballsack = [1, 1, 1, 2, 2, 3]

s = Solution()
s.topKFrequent(ballsack, 2)
