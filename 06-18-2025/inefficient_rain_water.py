from typing import *
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(1, n - 1):
            left_max, right_max = 0, 0
            for j in range(i - 1, -1, -1):
                left_max = max(left_max, height[j])
            
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])
            
            ans += max(min(left_max, right_max) - height[j], 0)
        
        return ans
    
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
            
        
            


            
                






    