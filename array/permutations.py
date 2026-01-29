class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # // let curr represent the thing you are building
        # // it could be an array or a combination of variables

        # function backtrack(curr) {
        #     if (base case) {
        #         Increment or add to answer
        #         return
        #     }

        #     for (iterate over input) {
        #         Modify curr
        #         backtrack(curr)
        #         Undo whatever modification was done to curr
        #     }
        # }
        permutations = []
        def backtrack(curr_permutation):
            if len(curr_permutation) == len(nums):
                permutations.append(curr_permutation[:]) # copy curr_permutation?
                return
            for num in nums:
                if num in curr_permutation: # violates constraint of uniqueness
                    continue
                curr_permutation.append(num) # choose num
                # print(f"{curr_permutation=}")
                backtrack(curr_permutation) # curr_permutation modified closer to basecase, explore to successor after adding num
                curr_permutation.pop() # unchoose num
        backtrack([])
        return permutations