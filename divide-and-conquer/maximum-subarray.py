class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
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

