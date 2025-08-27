from typing import *
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast: 
                break
        
        start, prev = 0, -1
        while True:
            temp = slow
            slow = nums[slow]
            start = nums[start]
            prev = temp
            if slow == start: 
                return prev




            

        










        