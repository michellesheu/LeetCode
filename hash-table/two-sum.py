class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        char_ind = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in char_ind:
                return [i, char_ind[pair]]
            char_ind[nums[i]] = i 
            