class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        right = len(nums) - 1
        
        # Iterate through the array with `i`
        i = 0
        while i <= right:
            if nums[i] == val:
                # Swap current element with the last element
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1  # Decrement right pointer
            else:
                i += 1  # Only increment if no swap occurs
        
        return right + 1
