from typing import *

class Solution:
    def minMoves(self, balance: List[int]) -> int:
        curr = 0
        n = len(balance)
        while curr < n and balance[curr] >= 0:
            curr += 1
        # print(f'curr: {curr}')
        if sum(balance) < 0: return -1
        if curr >= n: return 0
        d, ans = 1, 0

        while balance[curr] < 0:
            res = balance[curr - d] + balance[(curr + d) % n]
            ans += min(res * d, -balance[curr] * d)
            balance[curr] += res 
            d += 1

        return ans

# [1,2,-5,2]
