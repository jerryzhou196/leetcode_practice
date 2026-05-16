class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        desc_stack = []
        start, end = 0,0
        for i, num in enumerate(nums):
            while num < desc_stack[-1][1]:
                elem = desc_stack.pop()
                
                

            desc_stack.append(num)
            


        
    
        