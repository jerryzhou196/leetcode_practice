class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        for i in range(0, amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1

        for i in range(1, len(coins)):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if (j - coins[i]) >= 0: 
                    dp[i][j] += dp[i][j - coins[i]]

        return dp[len(coins) - 1][amount]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        @lru_cache(maxsize=1000000)
        def f(total=0, i=0):
            # print(total, i)
            if total > amount:
                return 0 
            if total == amount: 
                return 1
            if i >= len(coins):
                return 0
            
            return f(total + coins[i], i) + f(total, i + 1)
        
        return f()
            
        
        


