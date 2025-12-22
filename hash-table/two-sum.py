class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap entries as we iterate thru nums and check if complement is in hashmap
        num_ind = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_ind:
                return [num_ind[complement], i]
            num_ind[nums[i]] = i
         