from typing import *


class Solution:
    def candy(self, ratings: List[int]) -> int:
        hasChanged = True
        n = len(ratings)
        left2right = [1] * n
        right2left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i + 1]:
                left2right[i] = left2right[i - 1] + 1

        for i in range(n - 2, 0, -1):
            if ratings[i] > ratings[i - 1]:
                right2left[i] = right2left[i + 1] + 1

        return sum([max(left2right[i], right2left[i]) for i in range(n)])


s = Solution()
print(s.candy([5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 3, 2, 4, 10]))

# [1, 0, 2]
# [1, 1, 2]
# [1, 1, 2]

# ans
# [2, 1, 3]


# [5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 3, 2, 4, 10]
# [1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 1, 2, 1, 1, 1]
# [1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 1, 2, 1, 1, 1]
