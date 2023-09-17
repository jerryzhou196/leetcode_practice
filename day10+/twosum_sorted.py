from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while right > 0 and left < len(numbers) - 1 and left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left + 1, right + 1]
            if result < target:
                left += 1
            else:
                right -= 1


s = Solution()
print(s.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))
# [1,1,1,1,1,1,1,1,1,1,1,1,1]
