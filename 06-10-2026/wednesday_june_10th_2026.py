class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans_string = ""

        for i in range(n):
            dp[i][i] = True
            if 1 > len(ans_string):
                ans_string = s[i:i + 1]
            if i < n - 1 and s[i] == s[i + 1]: 
                dp[i][i + 1] = True
                if 2 > len(ans_string): 
                    ans_string = s[i:i + 2]
        
        for i in range(2, n):
            for j in range(n - i):
                # print(j, j + i)
                if dp[j + 1][j + i - 1] and s[j] == s[j + i]:
                    if i + 1 > len(ans_string): 
                        ans_string = s[j:j + i + 1]
                    dp[j][j + i] = True
        
        return ans_string

            
        
