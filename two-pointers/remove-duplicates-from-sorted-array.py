class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[uniq] = nums[r]
                uniq += 1
        return uniq