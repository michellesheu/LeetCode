class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for n in nums:
            print("n:", n)
            if n-1 not in nums:
                count = 1
                while n+1 in nums:
                    print("n+1:", n+1)
                    count += 1
                    n += 1
                max_count = max(count, max_count)
        return max_count