class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = 0
        # r = len(nums) - 1
        # i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums[i], nums[l] = nums[l], nums[i]
        #         l += 1
        #     elif nums[i] == 2:
        #         nums[i], nums[r] = nums[r], nums[i]
        #         r -= 1
        #     else:
        #         l+=1
        #         r-=1
        #     i += 1
        l = 0
        r = len(nums)-1
        i = 0
        while i <= r:
            n = nums[i]
            if n == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif n == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            if n == 1 or l > i or i > r:
                i += 1



