class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 0: empty, 1: hold 
        @lru_cache(maxsize=100000)
        def dfs(i=0, hold=0):
            # print(i, hold)
            if i >= len(prices):
                return 0

            if hold == 1: 
                return max(dfs(i + 1, 1), prices[i] + dfs(i + 2, 0))
            else:
                return max(dfs(i + 1, 1) - prices[i], dfs(i + 1, 0))


        return dfs()
 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # reset[i] = max(sold[i - 1], reset[i - 1])
        # held[i] = max(reset[i - 1] + nums[i], held[i - 1])
        # sold[i] = held[i - 1] + price[i]

        held, sold, reset = -float('inf'), -float('inf'), 0
    
        for price in prices: 
            old_held = held
            old_reset = reset
            reset = max(reset, sold)
            held = max(old_reset - price, held)
            sold = old_held + price
        
        return max(sold, held, reset)

