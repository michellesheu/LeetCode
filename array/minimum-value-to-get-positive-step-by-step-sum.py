class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current_sum = 0
        min_prefix_sum = 0
        
        for num in nums:
            current_sum += num
            min_prefix_sum = min(min_prefix_sum, current_sum)
        
        # Minimum starting value to ensure all sums are positive
        return 1 - min_prefix_sum
