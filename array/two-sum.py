class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: num val: ind
        # match = target - num and ind != curr 
        # hashmap for o(1) lookup o(n) space
        n_ind = {}
        for i in range(len(nums)):
            match = target - nums[i]
            curr = nums[i]
            if match in n_ind:
                return [i, n_ind[match]]
            n_ind[curr] = i
        return [-1,-1]