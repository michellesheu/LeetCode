class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  # Initialize with impossible value
        dp[0] = 0  # Base case
        
        # For each amount
        for i in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                if coin <= i:  # Can we use this coin?
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
        