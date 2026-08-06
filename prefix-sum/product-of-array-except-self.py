class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # why is this a hint: The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer? is it just saying we don't have to worry about overflow?
        # input: list of ints nums
        # output: list of product of prefix and suffix at each index
        # create list for ans output of len nums
        # iterate thru nums
        # this is brute force O(n^2) to recompute the product at every index
        # left = 0:i, right = i+1: , ans[i] = left * right
        # if at the ends of nums i.e. index 0 or -1, at index 0 left = 1 , at index -1 right = 1 
        # return ans
        ans = [1] * len(nums)
        prefix_prod = 1
        for i in range(len(nums)):
            ans[i] = prefix_prod
            prefix_prod *= nums[i]
        right_prod = 1
        n = len(nums)
        for i in range(n-1, -1, -1):
            ans[i] *= right_prod
            right_prod *= nums[i]
        return ans
