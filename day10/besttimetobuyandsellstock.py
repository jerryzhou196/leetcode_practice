[7, 1, 5, 3, 6, 4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        max_diff = 0
        for i in range(1, len(prices)):
            min_ = min(min_, prices[i])
            max_diff = max(max_diff, prices[i] - min_)
        return max_diff
        # max_ = 0
        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         if prices[i] > prices[j]:
        #             continue
        #         max_ = max(prices[j] - prices[i], max_)
        # return max_
