class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: list of nums
        # output: [i,j] i!=j nums[i]+nums[j]=target, diff indices of two nums that sum to target
        # make a hashmap of val:i bc we want to look for values in hashmap and keep track of their indices, complement = target - curr_val, if curr_val_i!= complement_val_j and complement in hashmap then return [curr_val_i, complement_val_j]
        val_ind = {}
        for i in range(len(nums)):
            val_ind[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            print(f"{complement=}")
            if complement in val_ind and i != val_ind[complement]:
                return [i,val_ind[complement]]
        return [-1,-1]