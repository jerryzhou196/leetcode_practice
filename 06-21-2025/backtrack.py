from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backTrack(curr = "", left_count = n, right_count = n):
            if right_count < left_count:
                return
            
            if left_count > 0:
                backTrack(curr+ '(', left_count - 1, right_count)
    
            if right_count> 0:
                backTrack(curr + ')', left_count, right_count - 1)
            
            if left_count == 0 and left_count == right_count: 
                ans.append(curr)
        
        backTrack()
        return ans

s = Solution()
print(s.generateParenthesis(5))
            
            
                


