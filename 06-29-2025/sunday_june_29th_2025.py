from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def f(i, j):
            if i == j: return heights[i]
            smallest, smallest_index = 0, 0
            for index, e in enumerate(heights[i:j+1]):
                if e < smallest:
                    smallest, smallest_index = e, index
            
            print(f"{i} - {j} with smallested: {smallest} at {smallest_index}")
            return max(
                    (j - i + 1) * smallest, 
                       f(i, smallest_index - 1),
                       f(j, smallest_index + 1)
                       )
        
        return f(0, len(heights) - 1)
                









        