class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def maxMoney(i):
            if i == 0: return nums[0]
            if i == 1: return max(nums[0], nums[1])
            if i in dp: 
                return dp[i]
            dp[i] = max(maxMoney(i - 2) + nums[i], maxMoney(i - 1))
            return dp[i]
        
        return maxMoney(len(nums) - 1)
