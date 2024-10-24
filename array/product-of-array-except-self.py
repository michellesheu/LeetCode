class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod, suffix_prod, prod = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        prefix_prod[0] = 1
        for i in range(1,len(nums)):
            prefix_prod[i] = prefix_prod[i-1]*nums[i-1]
        suffix_prod[len(nums)-1] = 1
        for i in reversed(range(len(nums)-1)):
            suffix_prod[i] = suffix_prod[i+1] * nums[i+1]
        for i in range(len(nums)):
            prod[i] = prefix_prod[i] * suffix_prod[i]
        return prod