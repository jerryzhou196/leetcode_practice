class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def topDown(i):
            if i == 0 or i == 1: 
                return 0
            if i in memo: 
                return memo[i]
            memo[i] = min(topDown(i - 1) + cost[i - 1], topDown(i - 2) + cost[i - 2])
            return memo[i]
        
        return topDown(len(cost))
            
            
            
            

            
        