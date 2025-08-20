class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        input: int array nums each elem represents max jump from that index
        output: return true if you can reach n-1th index else false
        m: greedy
        if n-2 index is 0, then u can't reach n-1
        if n -2
        '''
        farthest_jump = 0
        n = len(nums)
        for i, max_jump in enumerate(nums):
            if i > farthest_jump:
                return False
            farthest_jump = max(farthest_jump, i + max_jump)
            if farthest_jump >= n-1:
                return True