class Solution:
    def numDecodings(self, s: str) -> int:
        def isValid(c):
            if c[0] == '0': return False
            return 1 <= int(c) <= 26

        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 1 if isValid(s[0]) else 0

        if n <= 1: return dp[0]
        dp[1] = 0
        if isValid(s[1]):
            dp[1] = dp[0]
        if isValid(s[0] + s[1]):
            dp[1] += 1

        for i in range(2, n): 
            dp[i] = 0
            if isValid(s[i]):
                dp[i] += dp[i - 1]
            if isValid(s[i - 1] + s[i]):
                dp[i] += dp[i - 2]
        
        return dp[n - 1]
            
            
            


        # dp[i] = dp[i - 1] + 1 if isValid(s[i] + s[i - 1]) and s[i] + s[i - 1] <= 26 else dp[i - 1]
        # return 5
        
