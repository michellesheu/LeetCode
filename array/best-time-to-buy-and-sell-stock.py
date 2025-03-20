class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # update max profit if curr diff is > curr max 
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit