class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        longest_increasing = 1
        prev_increasing  = 0
        k = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                longest_increasing += 1
            elif nums[i] >= nums[i+1]:
                k = max(min(longest_increasing, prev_increasing), longest_increasing//2, k)
                prev_increasing = longest_increasing
                longest_increasing = 1
            k = max(min(longest_increasing, prev_increasing), longest_increasing//2, k)
        return k
               
            