from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        wanted = {}
        max_length = 0
        for element in nums:
            if element not in wanted:
                shared_object = [1]
                if element + 1 in wanted:
                    wanted[element + 1].push(shared_object)
                else:
                    wanted[element + 1] = [shared_object]
                if element - 1 in wanted:
                    wanted[element - 1].push(shared_object)
                else:
                    wanted[element - 1] = [shared_object]
            else:
                respective_objects = wanted[element]
                for match in respective_objects:
                    match[0] += 1
                    max_length = max(max_length, match[0])

                del wanted[element]
                if element + 1 in wanted:
                    


        return max_length


s = Solution()
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(s.longestConsecutive(nums))
