class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr = [], seen=set()): 
            if len(curr) == len(nums):
                ans.append(curr[:])
                return 
            
            for num in nums:
                if not num in seen:
                    seen.add(num)
                    curr.append(num)
                    backtrack(curr, seen)
                    seen.remove(num)
                    curr.pop()
        
        backtrack()
        return ans



        