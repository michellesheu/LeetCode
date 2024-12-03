class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle edge case of an empty array

        # Initialize the slow pointer
        i = 0

        # Iterate through the array with the fast pointer
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # Found a unique element
                i += 1             # Move the slow pointer
                nums[i] = nums[j]  # Update the position with the unique element

        return i + 1  # Length of the array with unique elements