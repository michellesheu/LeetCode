class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [0] * len(nums)
        prod[0] = 1
        for i in range(1,len(nums)):
            prod[i] = prod[i-1]*nums[i-1]
        suffix = 1
        for i in reversed(range(len(nums))):
            prod[i] = prod[i] * suffix
            suffix *= nums[i]
        return prod