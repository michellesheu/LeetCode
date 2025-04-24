class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_ind = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_ind:
                return [i,num_to_ind[complement]]
            num_to_ind[nums[i]] = i
        return [-1,-1]