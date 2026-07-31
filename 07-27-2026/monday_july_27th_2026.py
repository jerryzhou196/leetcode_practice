class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_diff = 0
        largest, smallest = arrays[0][0], arrays[0][-1] 
        for array in arrays:
            max_diff = max(abs(array[-1] - smallest), max_diff)
            max_diff = max(abs(array[0] - largest), max_diff)
            
            largest = max(largest, array[-1])
            smallest = min(smallest, array[0])
    
        return max_diff
            
