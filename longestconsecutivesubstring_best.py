from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = {}
        max_length = 0
        if len(nums) == 1:
            return 1

        for element in nums:
            nums_set[element] = element

        for element in nums:
            if not element - 1 in nums and element + 1 in nums:
                pointer = element
                while pointer in nums:
                    pointer += 1
                max_length = max(max_length, pointer - element)

        return max_length


s = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(nums))
