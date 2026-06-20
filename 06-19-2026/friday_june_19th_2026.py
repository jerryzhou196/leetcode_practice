class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)


        dp = [0] * (m + 1)
        # dp[0] = 1 

        # dp[i][j]: subsequences in s[:j] that match to t[:i]
        # dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        # print(dp)

        for i in range(1, n + 1):
            next_dp = [0] * (m + 1)
            dp[0] = 1
            for j in range(1, m + 1):
                next_dp[j] = dp[j]
                if s[i - 1] == t[j - 1]:
                    next_dp[j] += dp[j - 1]
            dp = next_dp
        
        return dp[m]
            




