from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        local_max = 0

        for i in range(n):
            left_max[i] = local_max
            local_max = max(height[i], local_max)

        local_max = 0

        for i in range(n - 1, -1, -1):
            right_max[i] = local_max
            local_max = max(height[i], local_max)

        ans = 0
        for i in range(n):
            ans += max(min(left_max[i], right_max[i]) - height[i], 0)
        
        return ans

s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])


        








s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
            
        
            


            
                






    