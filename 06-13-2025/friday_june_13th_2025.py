import heapq
from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        stack = []
        ans = []
        minChar = 'a'
        count = Counter(s)
        for char in s:
            stack.append(char)
            count[char] -= 1
            while minChar != 'z' and count[minChar] == 0:
                minChar = chr(ord(minChar) + 1)
            while stack and stack[-1] <= minChar:
                ans.append(stack.pop())
        
        return "".join(ans)

s = Solution()
print(s.robotWithString("bzzzzzzzzzzzzzzzzza"))









    
        