class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target in the left sorted half
                else:
                    left = mid + 1   # Target in the right unsorted half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target in the right sorted half
                else:
                    right = mid - 1  # Target in the left unsorted half

        return -1  # Target not found