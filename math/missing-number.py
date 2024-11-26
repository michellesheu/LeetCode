class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        no_dupes = set(nums)
        n = len(nums)
        for i in range(n+1):
            if i not in no_dupes:
                return i
        