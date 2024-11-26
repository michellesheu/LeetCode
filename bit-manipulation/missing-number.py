class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing_num = n
        for i in range(n):
            missing_num ^=i
            missing_num ^= nums[i]

        return missing_num
        