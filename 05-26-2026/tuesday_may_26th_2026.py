class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        if len(nums) == 1: return 0
        
        jumps = 0
        i = 0
        maximum_distance = nums[0] 
        can_jump = 1 
        while True: 
            start = i + 1
            # print(start, maximum_distance + 1)
            for j in range(start, maximum_distance + 1): 
                if j >= n - 1: return jumps + 1
                can_jump = max(j + nums[j], can_jump)
                i += 1

            jumps += 1
            maximum_distance = can_jump

# [2, 2, 4, 1000, 0, 0, 0, 1]
