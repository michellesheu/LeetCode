class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr = 0
        min_len = float("inf")
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                min_len = min(r - l + 1, min_len)
                curr -= nums[l]
                l += 1
        return min_len if min_len != float("inf") else 0 

