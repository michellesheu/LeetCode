class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down 
        # 1. define a recursive function dp that returns the min cost up to ith index of cost array
        # 2. base case is len(cost) == 1, pay cost[0]
        # 2. len(cost) == 2, return min(cost[0], cost[1])
        # 3. top floor is the index out of bounds of cost array
        # 4. recurrence relation is min(dp(i-1)+cost[i], dp(i-2)+cost[i])
        # 5. memoize expensive function calls to reduce duplicate computations

        # 1.
        @cache
        def dp(i):
            # 2.
            if i <= 1:
                return 0
            return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
        n = len(cost)
        return dp(n)
            
            