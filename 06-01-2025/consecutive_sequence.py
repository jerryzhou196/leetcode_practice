from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set(nums)
        max_streak = 0
        for num in exists:
            if num - 1 not in exists:
                streak = 1
                curr = num + 1
                while curr in exists:
                    streak += 1
                    curr += 1
                max_streak = max(max_streak, streak)

        return max_streak


s = Solution()
s.longestConsecutive([1, 2, 4, 5, 7, 8, 10, 11, 13, 14])
