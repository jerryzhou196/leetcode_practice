class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = [0, 1]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 2]
        
        for length in range(2, len(s)):
            for start in range(n - length):
                # print(start, start + length)
                if s[start] == s[start + length] and dp[start + 1][start + length - 1]:
                    dp[start][start + length] = True
                    ans = [start, start + length + 1]
        
        return s[ans[0]:ans[1]]
