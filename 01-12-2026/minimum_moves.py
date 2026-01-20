from typing import *

class Solution:
    def minMoves(self, A: List[int]) -> int:
        n = len(A)
        j = -1
        for i, a in enumerate(A):
            if a < 0:
                j = i
        if j < 0:
            return 0
        if sum(A) < 0:
            return -1
        res = 0
        d = 0
        while A[j] < 0:
            d += 1
            storage = A[(j + d) % n] + A[j - d]
            res += min(-A[j], storage) * d
            A[j] += storage
        return res

s = Solution()
s.minMoves([5, 1, -4, 4, 7, 10])
