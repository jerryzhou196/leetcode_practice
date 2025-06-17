from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i, n = 0, len(nums)
        while i < n:
            x, y = i + 1, n - 1
            target = 0 - nums[i]
            while x < y:
                if nums[x] + nums[y] == target:
                    ans.append([nums[i], nums[x], nums[y]])
                    x += 1
                    while x < n and nums[x] == nums[x - 1]:
                        x += 1
                elif nums[x] + nums[y] < target:
                    x += 1
                else:
                    y -= 1

            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1
        
        return ans
    

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
                






