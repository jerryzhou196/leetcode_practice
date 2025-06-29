from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        hottest = 0
        for i in range(n - 1, -1, -1):
            if temperatures[i] < hottest:
                days = 1
                while temperatures[i] >= temperatures[i + days]:
                    days += ans[i + days]
                ans[i] = days

            hottest = max(hottest, temperatures[i])

        return ans
