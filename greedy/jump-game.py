class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Initialize the maximum reachable index
        reachable = 0
        
        # Traverse each index
        for i in range(len(nums)):
            # If the current index is beyond the maximum reachable, return False
            if i > reachable:
                return False
            
            # Update the maximum reachable index
            reachable = max(reachable, i + nums[i])
            
            # Early exit if we already reached the last index
            if reachable >= len(nums) - 1:
                return True
        
        return False
