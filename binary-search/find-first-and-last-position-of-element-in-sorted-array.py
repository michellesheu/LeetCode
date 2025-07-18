
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        result = [-1, -1]
        
        # 1. Search for the left boundary
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        # If the target wasn't found, return [-1, -1]
        if nums[left] != target:
            return result
        
        result[0] = left

        # 2. Search for the right boundary
        # We can reuse 'left' from the first search as the starting point.
        # 'right' needs to be reset.
        right = len(nums) - 1
        while left < right:
            # Use the right-biased mid to avoid an infinite loop
            mid = (left + right) // 2 + 1 
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        
        result[1] = right # or left, since they are equal
        
        return result