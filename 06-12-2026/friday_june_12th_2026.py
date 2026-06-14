class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp, smallest = [0 for _ in range(n)], [0 for _ in range(n)]

        dp[0], smallest[0] = nums[0], nums[0]
        for i in range(1, n): 
            dp[i] = max(dp[i - 1] * nums[i], smallest[i - 1] * nums[i], nums[i])
            smallest[i] = min(smallest[i - 1] * nums[i], dp[i - 1] * nums[i], nums[i])
        
        return max(dp)

        # dp[i] = dp[i - 1] * nums[i] if nums[i] > 0 else min[i - 1] * nums[i] if nums < 0
       
