class Solution:
    def lastSubstring(self, word):
        n = len(word)
        i, j, k = 0, 1, 0
        while j + k < n:
            if word[i + k] < word[j + k]:
                i, j = j, j + 1 
                k = 0
            elif word[i + k] > word[j + k]:
                j += 1
                k = 0
            else:
                k += 1

        return word[i:]
    
    def answerString(self, word: str, numFriends: int) -> str:
        last = self.lastSubstring(word)
        n, m = len(word), len(last)
        return last[:min(n - numFriends + 1, m)]

s = Solution()    
print(s.answerString("asfesfez", 3))