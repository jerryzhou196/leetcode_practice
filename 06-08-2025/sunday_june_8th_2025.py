from collections import defaultdict
from typing import *


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        def dfs(curr, can_go):
            if status[curr] == 1:
                total = candies[curr]
                for key in keys[curr]:
                    status[key] = 1
                    if key in can_go:
                        total += dfs(key, can_go)
                for box in containedBoxes[curr]:
                    total += dfs(box, can_go)
            else:
                can_go.add(curr)
                total = 0

            return total

        can_go = set()
        ans = 0

        for box in initialBoxes:
            status[box] = 1
            ans += dfs(box, can_go)

        return ans


status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
intialBoxes = [0]

s = Solution()
print(s.maxCandies(status, candies, keys, containedBoxes, intialBoxes))
