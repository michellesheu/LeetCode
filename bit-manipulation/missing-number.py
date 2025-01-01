class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        n = len(nums)
        for i in range(n+1):
            missing ^= i
        for n in nums:
            missing ^= n
        return missing