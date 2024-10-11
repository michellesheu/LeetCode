class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                max_sum = max(curr, max_sum)
        return max_sum
        # l = 0
        # biggest = float("-inf")
        # curr = 0
        # for r in range(len(nums)):
        #     curr += nums[r]
        #     if curr > biggest:
        #         biggest = curr
        #     else:
        #         curr -= nums[l]
        #         l += 1
        # return biggest

