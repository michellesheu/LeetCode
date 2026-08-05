class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: nums is a list of ints, target is an int
        # output: one solution a list of two different indices that sum to target
        # use a hashmap that keeps track of each num to index bc we want to keep track of indices that sum up to target
        # same num will update to latest index but we will return soln in this case 3:0 -> 3:1 as long as we check index is different
        # iterate thru nums and check if complement in hashmap already then return ans 
        num_ind = {}
        for i in range(len(nums)):
            num_ind[nums[i]] = i
        print(num_ind)
        for i in range(len(nums)):
            complement = target - nums[i]
            print(complement)
            if complement in num_ind and i!=num_ind[complement]:
                return [i,num_ind[complement]]
        return [-1,-1]
