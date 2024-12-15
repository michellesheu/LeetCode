class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        prefix_sum = 0
        for n in nums:
            prefix_sum += n
            min_prefix_sum = min(prefix_sum, min_prefix_sum)
        return 1 - min_prefix_sum