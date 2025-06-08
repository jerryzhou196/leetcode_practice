from typing import *


class Solution:
    def candy(self, ratings: List[int]) -> int:
        hasChanged = True
        n = len(ratings)
        count = [1] * n

        # ratings = [1, 2, 1, 1, 1, 2, 3, 4]
        iteration_count = 0
        print(f"ratings:      {ratings}")

        while hasChanged:
            hasChanged = False
            print(f"iteration #{iteration_count}: {count}")
            for i in range(n):
                if (
                    i != n - 1
                    and ratings[i] > ratings[i + 1]
                    and count[i] <= count[i + 1]
                ):
                    count[i] += 1
                    hasChanged = True

                if i != 0 and ratings[i] > ratings[i - 1] and count[i] <= count[i - 1]:
                    count[i] += 1
                    hasChanged = True

            iteration_count += 1

        return count


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
