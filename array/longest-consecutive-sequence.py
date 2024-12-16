class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for n in nums:
            print("n:", n)
            if n-1 not in nums:
                y = n+1
                while y in nums:
                    y += 1
                max_len = max(max_len, y - n)
        return max_len