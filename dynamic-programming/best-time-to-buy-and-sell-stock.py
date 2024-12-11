class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            min_buy = min(prices[i], min_buy)
            max_profit = max(prices[i] - min_buy, max_profit)
        return max_profit