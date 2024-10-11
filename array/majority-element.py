class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore Voting algo
        curr_candidate = nums[0]
        count = 0
        for i in range(1, len(nums)):
            if curr_candidate == nums[i]:
                count += 1
            if count == 0:
                curr_candidate = nums[i]
        return curr_candidate