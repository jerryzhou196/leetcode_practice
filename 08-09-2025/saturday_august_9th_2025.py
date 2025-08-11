
from typing import *

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def store(n=0):
            if nums[n] != n: 
                temp = nums[n]
                nums[n] = n
                return store(temp)
            else:
                return n

        return store()


# iteration 0: [1, -3, -4, -2, -2]
# iteration 1: [1, -3, 4, 2, 2]
# iteration 2: [1, -3, 4,-2, 2]
# iteration 3: [1, -3, 4,-2,-2]
# iteration 4: [1, -3, 4,-2,-2]

