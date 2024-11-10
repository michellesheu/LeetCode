class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = -1
        r = len(nums)
        for i, n in enumerate(nums):
            if i >= r:
                break
            if n == 0:
                l += 1
                nums[l], nums[i] = nums[i], nums[l]
            elif n == 2:
                r -= 1
                nums[r], nums[i] = nums[i], nums[r]
