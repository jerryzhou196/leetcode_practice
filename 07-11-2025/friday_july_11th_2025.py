class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, ans = 0, 0
        for r in range(len(prices)):
            if prices[r] > prices[l]: 
                left = r
            else:
                ans = max(ans, prices[l] - prices[r])
        return ans

if __name__ == "__main__":
    main()
