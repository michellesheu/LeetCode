class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        char_ind = {}
        for i in range(len(nums)):
            char_ind[nums[i]] = i
        print(char_ind)
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in char_ind and i != char_ind[pair]:
                return [i, char_ind[pair]]