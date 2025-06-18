from typing import *
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, 1

        total_area = 0
        potential_area = 0

        # left to right pass
        while j < n:
            if height[j] >= height[i]:
                total_area += potential_area
                potential_area = 0
                i = j 
                j = j + 1
            else:
                potential_area += height[i] - height[j]
                j += 1

        i, j = n - 1, n - 2
        potential_area = 0
        
        while j >= 0:
            if height[j] > height[i]:
                total_area += potential_area
                potential_area = 0
                i = j 
                j = j - 1
            else:
                potential_area += height[i] - height[j]
                j -= 1

        
        return total_area
    
s = Solution()
print(s.trap([2,0,2]))