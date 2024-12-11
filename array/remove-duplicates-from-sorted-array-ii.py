class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # If array length <= 2, return it as is.

        i = 2  # Start from index 2 since the first two are always allowed

        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:  # Check if current is not a third duplicate
                nums[i] = nums[j]
                i += 1
        
        return i
