class Solution:
    def rob(self, nums: List[int]) -> int:

        def steal(start, end):
            dp = [0 for _ in range(end)]
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start], nums[start + 1])
            n = len(nums)
        
            for i in range(start + 2, end): 
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
            return dp[end - 1]
    
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        if len(nums) == 1: 
            return nums[0]

        return max(steal(0, len(nums) - 1), steal(1, len(nums)))

        # dp[i]: maximum money up to ith house 
        # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]) 
        
        
