class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        max_profit = 0
        for j in range(1,len(prices)):
            if prices[j] > prices[i]:
                profit += prices[j] - prices[i]
                max_profit = max(profit, max_profit)
            i += 1
        return max_profit