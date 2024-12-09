class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Iterate through the prices array from the second element
        # Compare each price with the previous day's price
        # If the current price is higher, add the difference to the total profit
        # This approach ensures you capture every possible profitable transaction
        if len(prices) == 1:
            return 0
        total = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = prices[i] - prices[i-1]
                total += profit
        return total 


