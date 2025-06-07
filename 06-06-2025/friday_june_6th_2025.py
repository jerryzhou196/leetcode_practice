from typing import *

class Solution:
    def candy(self, ratings: List[int]) -> int:
        didChange = True 
        n = len(ratings)
        count = [1] * n

        while didChange:
            didChange = False
            for i in range(n):
                if (
                        (i != n - 1 and 
                        ratings[i] > ratings[i + 1]
                        and count[i] <= count[i + 1]
                        ) 
                    or 
                        (i != 0 and 
                        ratings[i] > ratings[i - 1]
                        and count[i] <= count[i - 1]
                        )
                    ):
                    count[i] += 1
                    didChange = True

        return sum(count)
        

s = Solution()
print(s.candy([5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 3, 2, 4, 10]))