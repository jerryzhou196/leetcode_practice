class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        ans = None

        for i in range(n):
            if not ans: 
                ans = word[i: min(n - numFriends + i + 1, n)]
            else:
                ans = min(ans, word[i: min(n - numFriends + i + 1, n)])

        return ans 
        

s = Solution()
print(s.answerString("arcslogger", 5))
        
