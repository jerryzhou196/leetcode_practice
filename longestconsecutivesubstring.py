from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        biggest = max(nums)
        smallest = 0 - min(nums) if min(nums) < 0 else 0

        number_line = [None for index in range(biggest + smallest + 1)]

        for element in nums:
            number_line[element + smallest] = True

        max_length = 0
        length = 0

        for element in number_line:
            if element:
                length += 1
                max_length = max(length, max_length)
            else:
                length = 0

        return max_length


s = Solution()
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(s.longestConsecutive(nums))
