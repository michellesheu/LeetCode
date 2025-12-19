class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # input: array of nums
        # output: return true if dup; else false
        # use a set to get only unique numbers if len of set not the same as nums length then return false
        return len(set(nums)) != len(nums) 